import json
from typing import Dict, Any
import tiktoken
import numpy as np
from numpy.linalg import norm
from sklearn.feature_extraction.text import TfidfVectorizer
import os
import shutil
import subprocess
import Levenshtein

from gensim.models import Word2Vec
from nltk.tokenize import sent_tokenize, word_tokenize

import nltk
nltk.download('punkt')


ENCODING = tiktoken.get_encoding("cl100k_base")
COMPILER_PATH = "./compiler/compiler.jar"
WIDGETS_PATH = "./base/widgets.bdd"
DSL_AST_EXTRACTOR_PATH = os.path.join(".","compiler", "DSL_AST_Extractor.jar")

# Create wrapper for measuring the time it takes to run the function
def timer(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.__name__} took {end - start:.4f} seconds to run")
        return result
    return wrapper


def load_json_file(file_path: str) -> Dict[str, Any]:
    """Load a JSON file and return its content."""
    with open(file_path, "r", encoding="utf-8") as json_file:
        return json.load(json_file)


def load_text_file(file_path: str) -> str:
    """Load a text file and return its content as a string."""
    with open(file_path, "r", encoding="utf-8") as prompt_file:
        return prompt_file.read()
    

def save_json(data: Dict[str, Any], output_path: str) -> None:
    """Save the errors to a file."""
    with open(output_path, "w", encoding="utf-8") as output_file:
        output_file.write(data)


@timer
def get_word2vec_similarity(s1: str, s2: str) -> float:
    # Tokenize the strings into sentences
    sentences_s1 = sent_tokenize(s1)
    sentences_s2 = sent_tokenize(s2)

    # Tokenize each sentence into words and combine
    sentences = [word_tokenize(sent) for sent in sentences_s1 + sentences_s2]

    # Train a Word2Vec model
    model = Word2Vec(sentences, min_count=1)

    # Calculate the similarity between the two strings as the average similarity of their words
    similarities = []
    for word in word_tokenize(s1):
        if word in model.wv.key_to_index:  # Use key_to_index instead of vocab
            similarities.append(np.mean([model.wv.similarity(word, word2) for word2 in word_tokenize(s2) if word2 in model.wv.key_to_index]))

    return np.mean(similarities)


@timer
def get_cosine_similarity(s1: str, s2: str) -> float:
    A = np.array(ENCODING.encode(s1))
    B = np.array(ENCODING.encode(s2))

    if A.shape != B.shape:
        # Resize A and/or B
        A = np.resize(A, B.shape)

    return np.dot(A, B)/(norm(A)*norm(B))


@timer
def get_tfidf_similarity(s1: str, s2: str) -> float:
    # TODO do not remove stop words (stop words are important in this case)
    vect = TfidfVectorizer(min_df=1, stop_words="english")
    tfidf = vect.fit_transform([s1, s2])
    pairwise_similarity = tfidf * tfidf.T
    return pairwise_similarity.toarray()[0, 1]


@timer
def get_levenshtein_distance(s1: str, s2: str) -> int:
    return Levenshtein.distance(s1, s2)


@timer
def get_jaccard_similarity(s1: str, s2: str):
    a = set(s1.split())
    b = set(s2.split())
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))


@timer
def get_ast(file_path: str) -> None:
    """Get the abstract syntax tree of all files with a specific extension within a folder."""
    completed_process = subprocess.run(["java", "-jar", DSL_AST_EXTRACTOR_PATH, file_path], stdout=subprocess.PIPE, text=True)
    return completed_process.stdout


def get_similarity_score(possible_solution_path: str, generated_solution_path: str) -> Dict[str, Any]:
    """Get the similarity score of the generated .bdd file compared to the possible solution .bdd file."""
    possible_solution = load_text_file(possible_solution_path)
    generated_solution = load_text_file(generated_solution_path)

    # possible_solution_ast = get_ast(possible_solution_path)
    # generated_solution_ast = get_ast(generated_solution_path)
    # ast_tfidf_similarity = get_tfidf_similarity(possible_solution_ast, generated_solution_ast)
    # ast_levenstein_distance = get_levenshtein_distance(possible_solution_ast, generated_solution_ast)
    # ast_cosine_similarity = get_cosine_similarity(possible_solution_ast, generated_solution_ast)
    # ast_word2vec_similarity = get_word2vec_similarity(possible_solution_ast, generated_solution_ast)

    cosine_similarity = get_cosine_similarity(possible_solution, generated_solution)
    levenshtein_distance = get_levenshtein_distance(possible_solution, generated_solution)
    tfidf_similarity = get_tfidf_similarity(possible_solution, generated_solution)
    jaccard_similarity = get_jaccard_similarity(possible_solution, generated_solution)
    # word2vec_similarity = get_word2vec_similarity(possible_solution, generated_solution)

    similarity = {
        "cosine_similarity": float(f"{cosine_similarity:.4f}"),
        "levenshtein_distance": levenshtein_distance,
        "tfidf_similarity": float(f"{tfidf_similarity:.4f}"),
        "jaccard_similarity": float(f"{jaccard_similarity:.4f}"),
        # "word2vec_similarity": f"{word2vec_similarity:.4f}",
        # "ast_tfidf_similarity": f"{ast_tfidf_similarity:.4f}",
        # "ast_levenstein_distance": ast_levenstein_distance,
        # "ast_cosine_similarity": f"{ast_cosine_similarity:.4f}",
        # "ast_word2vec_similarity": f"{ast_word2vec_similarity:.4f}",

    }

    return similarity


def get_score_of_generated_data(possible_solution_folder_path: str, generated_folder_path: str) -> str:
    """Get the similarity score of each generated .bdd file compared to the possible solution .bdd files."""
    scores = {}
    for possible_solution in os.listdir(possible_solution_folder_path):
        for generated in os.listdir(generated_folder_path):
            print(generated)
            if not possible_solution.endswith(".bdd"): continue
            if not generated.endswith(".bdd"): continue
            if possible_solution != generated.split("_")[0] + ".bdd": continue
            
            scores[generated] = get_similarity_score(
                os.path.join(possible_solution_folder_path, possible_solution), 
                os.path.join(generated_folder_path, generated))
            
            scores[generated]["compiler_log"] = compile_model(os.path.join(generated_folder_path, generated))

    return json.dumps(scores, sort_keys=True, indent=4, ensure_ascii=False)


def get_score_of_generated_data_2(ground_truth_bdd_path: str, generated_folder_path: str) -> str:

    scores = {}
    for version in os.listdir(generated_folder_path):
        version_path = os.path.join(generated_folder_path, version)
        if not os.path.isdir(version_path): continue
        print(version)
        scores[version] = {}

        for attempt in os.listdir(version_path):
            attempt_path = os.path.join(version_path, attempt)
            if not attempt.endswith(".bdd"): continue
            print(attempt)

            # id = version+"/"+attempt

            scores[version][attempt] = get_similarity_score(ground_truth_bdd_path, attempt_path)
            
            scores[version][attempt]["compiler_log"] = compile_model(attempt_path)

        
    return json.dumps(scores, sort_keys=True, indent=4, ensure_ascii=False)



@timer
def compile_model(dsl_file_path: str, compiler_path: str = COMPILER_PATH, widgets_path: str = WIDGETS_PATH) -> list[str]:
    """Compile the given .bdd file using the BDD-DSL compiler and return the output as a list of strings."""
    temp_dir = "temp"
    temp_dir_path = os.path.join(os.getcwd(), temp_dir)

    os.makedirs(temp_dir_path, exist_ok=True)
    shutil.copy(widgets_path, temp_dir_path)
    shutil.copy(dsl_file_path, temp_dir_path)
    shutil.copy(compiler_path, temp_dir_path)
    
    new_compiler_path = os.path.join(temp_dir_path, os.path.split(compiler_path)[1])

    completed_process = subprocess.run(["java", "-jar", new_compiler_path, os.path.join(".", temp_dir)], stdout=subprocess.PIPE, text=True)

    output = completed_process.stdout

    output = output.split("\n") # split based on newline
    output = list(filter(None, output)) # remove empty strings

    shutil.rmtree(temp_dir_path, ignore_errors=True)

    return output


def main():
    possible_solution_path = "./possible_solutions"
    ground_truth = "./possible_solutions/eCommerce.bdd"
    generated_path = "./generated"

    # scores = get_score_of_generated_data(possible_solution_path, generated_path)
    # save_json(scores, "similarity_scores.json")

    scores = get_score_of_generated_data_2(ground_truth, generated_path)
    print(scores)
    save_json(scores, "similarity_scores_2.json")


if __name__ == "__main__":
    main()

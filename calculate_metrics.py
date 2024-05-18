import json
from typing import Dict, Any
# import tiktoken
# import numpy as np
# from numpy.linalg import norm
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os
import shutil
import subprocess
import Levenshtein
import argparse
from jarowinkler import *
import difflib

# from gensim.models import Word2Vec
# from nltk.tokenize import sent_tokenize, word_tokenize

# import nltk
# nltk.download('punkt')


# ENCODING = tiktoken.get_encoding("cl100k_base")
COMPILER_PATH = "./compiler/compiler.jar"
WIDGETS_PATH = "./base/widgets.bdd"
DSL_AST_EXTRACTOR_PATH = os.path.join(".","compiler", "DSL_AST_Extractor_3.jar")

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
def get_tfidf_similarity(s1: str, s2: str) -> float:
    """The TF-IDF similarity is calculated as the cosine similarity between the TF-IDF vectors of the two strings.
    
    Parameters:
    
    s1 (str): The first string.
    s2 (str): The second string.
    
    Returns:
    
    float: The TF-IDF similarity between the two strings.
    """
    vect = TfidfVectorizer(min_df=1)
    tfidf = vect.fit_transform([s1, s2])
    pairwise_similarity = tfidf * tfidf.T
    return pairwise_similarity.toarray()[0, 1]


@timer
def get_tfidf_stopwords_similarity(s1: str, s2: str) -> float:
    """The TF-IDF similarity is calculated as the cosine similarity between the TF-IDF vectors of the two strings.
    
    Parameters:
    
    s1 (str): The first string.
    s2 (str): The second string.
    
    Returns:
    
    float: The TF-IDF similarity between the two strings.
    """
    vect = TfidfVectorizer(min_df=1, stop_words="english")
    tfidf = vect.fit_transform([s1, s2])
    pairwise_similarity = tfidf * tfidf.T
    return pairwise_similarity.toarray()[0, 1]


@timer
def get_levenshtein_distance(s1: str, s2: str) -> int:
    """Calculate the Levenshtein distance between two strings."""
    return Levenshtein.distance(s1, s2)


@timer
def get_token_levenshtein_distance(s1, s2):
    """Calculate the Levenshtein distance between two strings based on tokens (words)."""
    # Split the strings into tokens based on whitespace
    tokens1 = s1.split()
    tokens2 = s2.split()

    # Initialize the matrix with zeros
    d = [[0 for _ in range(len(tokens2) + 1)] for _ in range(len(tokens1) + 1)]

    # Populate the first column and first row of the matrix
    for i in range(len(tokens1) + 1):
        d[i][0] = i
    for j in range(len(tokens2) + 1):
        d[0][j] = j

    # Iterate over the matrix and fill it in
    for i in range(1, len(tokens1) + 1):
        for j in range(1, len(tokens2) + 1):
            # Check if tokens are the same
            if tokens1[i - 1] == tokens2[j - 1]:
                cost = 0
            else:
                cost = 1
            
            # Calculate distances for the three operations
            deletion = d[i - 1][j] + 1
            insertion = d[i][j - 1] + 1
            substitution = d[i - 1][j - 1] + cost

            # Choose the minimum distance
            d[i][j] = min(insertion, deletion, substitution)

    # The distance is in the bottom-right corner of the matrix
    return d[len(tokens1)][len(tokens2)]


@timer
def get_longest_common_subsequence(s1: str, s2: str) -> int:
    """Get the longest common subsequence of two strings."""
    match = difflib.SequenceMatcher(None, s1, s2)
    lcs = "".join(s1[x[0]:x[0]+x[2]] for x in match.get_matching_blocks()[:-1])
    return lcs


@timer
def get_jaccard_similarity(s1: str, s2: str):
    a = set(s1.split())
    b = set(s2.split())
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))


@timer
def get_jaro_winkler_similarity(s1: str, s2: str) -> float:
    return jarowinkler_similarity(s1, s2)


@timer
def get_bag_of_words_similarity(s1: str, s2: str) -> float:
    """Calculate the similarity between two strings based on the bag of words model."""
    vectorizer = CountVectorizer().fit_transform([s1, s2])
    vectors = vectorizer.toarray()
    similarity = cosine_similarity(vectors)
    return similarity[0][1]


@timer
def get_ast(file_path: str) -> None:
    """Get the abstract syntax tree of all files with a specific extension within a folder."""
    completed_process = subprocess.run(["java", "-jar", DSL_AST_EXTRACTOR_PATH, file_path], stdout=subprocess.PIPE, text=True)
    return completed_process.stdout


def get_similarity_score(possible_solution_path: str, generated_solution_path: str) -> Dict[str, Any]:
    """Get the similarity score of the generated .bdd file compared to the possible solution .bdd file."""
    possible_solution = load_text_file(possible_solution_path)
    generated_solution = load_text_file(generated_solution_path)

    possible_solution_ast = get_ast(possible_solution_path)
    generated_solution_ast = get_ast(generated_solution_path)
    print(possible_solution_ast)

    ast_tfidf_similarity = get_tfidf_similarity(possible_solution_ast, generated_solution_ast)
    ast_tfidf_stopwords_similarity = get_tfidf_stopwords_similarity(possible_solution_ast, generated_solution_ast)
    ast_levenstein_distance = get_levenshtein_distance(possible_solution_ast, generated_solution_ast)
    ast_jaccard_similarity = get_jaccard_similarity(possible_solution_ast, generated_solution_ast)
    ast_levenshtein_token_distance = get_token_levenshtein_distance(possible_solution_ast, generated_solution_ast)
    ast_longest_common_subsequence = get_longest_common_subsequence(possible_solution_ast, generated_solution_ast)
    ast_length_of_longest_common_subsequence = len(ast_longest_common_subsequence) / min(len(possible_solution_ast), len(generated_solution_ast))
    ast_jaro_winkler_similarity = get_jaro_winkler_similarity(possible_solution_ast, generated_solution_ast)
    ast_bag_of_words_similarity = get_bag_of_words_similarity(possible_solution_ast, generated_solution_ast)

    tfidf_similarity = get_tfidf_similarity(possible_solution, generated_solution)
    tfidf_stopwords_similarity = get_tfidf_stopwords_similarity(possible_solution, generated_solution)
    levenshtein_distance = get_levenshtein_distance(possible_solution, generated_solution)
    jaccard_similarity = get_jaccard_similarity(possible_solution, generated_solution)
    levenshtein_token_distance = get_token_levenshtein_distance(possible_solution, generated_solution)
    longest_common_subsequence = get_longest_common_subsequence(possible_solution, generated_solution)
    length_of_longest_common_subsequence = len(longest_common_subsequence) / min(len(possible_solution), len(generated_solution))
    jaro_winkler_similarity = get_jaro_winkler_similarity(possible_solution, generated_solution)
    bag_of_words_similarity = get_bag_of_words_similarity(possible_solution, generated_solution)

    similarity = {
        "levenshtein_distance": levenshtein_distance,
        "tfidf_similarity": float(f"{tfidf_similarity:.4f}"),
        "tfidf_stopwords_similarity": float(f"{tfidf_stopwords_similarity:.4f}"),
        "jaccard_similarity": float(f"{jaccard_similarity:.4f}"),
        "levenshtein_distance_token": levenshtein_token_distance,
        "longest_common_subsequence": float(f"{length_of_longest_common_subsequence:.4f}"),
        "jaro_winkler_similarity": float(f"{jaro_winkler_similarity:.4f}"),
        "bag_of_words_similarity": float(f"{bag_of_words_similarity:.4f}"),
        "ast_tfidf_similarity": float(f"{ast_tfidf_similarity:.4f}"),
        "ast_levenstein_distance": ast_levenstein_distance,
        "ast_jaccard_similarity": float(f"{ast_jaccard_similarity:.4f}"),
        "ast_longest_common_subsequence": float(f"{ast_length_of_longest_common_subsequence:.4f}"),
        "ast_levenshtein_token_distance": ast_levenshtein_token_distance,
        "ast_jaro_winkler_similarity": float(f"{ast_jaro_winkler_similarity:.4f}"),
        "ast_bag_of_words_similarity": float(f"{ast_bag_of_words_similarity:.4f}"),
        "ast_tfidf_stopwords_similarity": float(f"{ast_tfidf_stopwords_similarity:.4f}")
    }

    return similarity


def get_score_of_generated_data(ground_truth_bdd_path: str, generated_folder_path: str) -> str:

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

            scores[version][attempt] = get_similarity_score(ground_truth_bdd_path, attempt_path)
            
            scores[version][attempt]["compiler_log"] = compile_model(attempt_path)

        
    return json.dumps(scores, sort_keys=True, indent=4, ensure_ascii=False)


def clean_llm_ouput(dsl_file_path: str) -> str:
    with open(dsl_file_path, 'r') as dsl_file:
        lines = dsl_file.readlines()

    start_idx = end_idx = None
    for idx, line in enumerate(lines):
        if '```' in line:
            if start_idx is None:
                start_idx = idx + 1  # Skip the line with "```"
            else:
                end_idx = idx  # Don't skip this line, as we want to remove everything after "```"
                break

    # Ensure we have valid start and end indices before extracting the content
    if start_idx is not None and end_idx is not None and start_idx < end_idx:
        cleaned_content = ''.join(lines[start_idx:end_idx])
    elif start_idx is not None:
        cleaned_content = ''.join(lines[start_idx:])  # If there's no ending "```", take everything after the starting one
    else:
        cleaned_content = ''.join(lines)

    return cleaned_content


@timer
def compile_model(dsl_file_path: str, compiler_path: str = COMPILER_PATH, widgets_path: str = WIDGETS_PATH, clean_output: bool = True) -> list[str]:
    """Compile the given .bdd file using the BDD-DSL compiler and return the output as a list of strings."""
    temp_dir = "temp"
    temp_dir_path = os.path.join(os.getcwd(), temp_dir)

    os.makedirs(temp_dir_path, exist_ok=True)
    shutil.copy(widgets_path, temp_dir_path)
    shutil.copy(compiler_path, temp_dir_path)

    new_dsl_file_path = os.path.join(temp_dir_path, os.path.basename(dsl_file_path))

    if clean_output:
        cleaned_content = clean_llm_ouput(dsl_file_path)
        
        with open(new_dsl_file_path, 'w') as cleaned_file:
            cleaned_file.write(cleaned_content)
    else:
        shutil.copy(dsl_file_path, new_dsl_file_path)

    new_compiler_path = os.path.join(temp_dir_path, os.path.split(compiler_path)[1])

    completed_process = subprocess.run(["java", "-jar", new_compiler_path, os.path.join(".", temp_dir)], stdout=subprocess.PIPE, text=True)

    output = completed_process.stdout

    output = output.split("\n") # split based on newline
    output = list(filter(None, output)) # remove empty strings

    shutil.rmtree(temp_dir_path, ignore_errors=True)

    return output


def main(ground_truth, generated_path, output_path = "output.json"):
    scores = get_score_of_generated_data(ground_truth, generated_path)
    print(scores)
    save_json(scores, output_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calculate metrics.')
    parser.add_argument('--ground-truth', type=str, required=True, help='Path to the ground truth file.')
    parser.add_argument('--folder-path', type=str, required=True, help='Path to the folder containing generated data.')
    parser.add_argument('--output', type=str, required=False, help='Path to the output file.')
    args = parser.parse_args()

    main(args.ground_truth, args.folder_path, args.output)
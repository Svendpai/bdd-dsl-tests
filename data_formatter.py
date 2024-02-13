import os
import subprocess
import argparse

DSL_AST_EXTRACTOR_PATH = os.path.join(".","compiler", "DSL_AST_Extractor.jar")
SOURCE_EXTENSION = '.bdd'
ESCAPE_MAPPINGS = {
    '\\': '\\\\',  # Escape backslashes
    '"': '\\"',    # Escape double quotes
    '\n': '\\n',   # Escape newlines
    '\t': '\\t'    # Escape tabs
}


def escape_text(content: str) -> str:
    """Escape backslashes, double quotes, newlines, and tabs in the given text."""
    for original, escaped in ESCAPE_MAPPINGS.items():
        content = content.replace(original, escaped)
    return content


def process_file(source_path: str, target_path: str) -> None:
    """Read the content of a file, escape it, and write it to a new file."""
    try:
        with open(source_path, 'r', encoding='utf-8') as source_file:
            content = source_file.read()
        escaped_content = escape_text(content)
        with open(target_path, 'w', encoding='utf-8') as target_file:
            target_file.write(escaped_content)
    except IOError as e:
        print(f"An error occurred while processing {source_path}: {e}")


def escape_files_in_folder(folder_path: str) -> None:
    """Escape characters in all files with a specific extension within a folder."""
    for file in os.listdir(folder_path):
        if file.endswith(SOURCE_EXTENSION):
            source_path = os.path.join(folder_path, file)
            target_path = source_path.replace(SOURCE_EXTENSION, "_escaped.txt")
            process_file(source_path, target_path)


def clean_folder_except_bdd(folder_path):
    for file in os.listdir(folder_path):
        if not file.endswith(SOURCE_EXTENSION):
            os.remove(os.path.join(folder_path, file))


def get_ast(folder_path: str) -> None:
    """Get the abstract syntax tree of all files with a specific extension within a folder."""
    for file in os.listdir(folder_path):
        if file.endswith(SOURCE_EXTENSION):
            source_path = os.path.join(folder_path, file)
            completed_process = subprocess.run(["java", "-jar", DSL_AST_EXTRACTOR_PATH, source_path], stdout=subprocess.PIPE, text=True)
            target_path = source_path.replace(SOURCE_EXTENSION, "_ast.txt")

            try:
                with open(target_path, "w") as target_file:
                    target_file.write(completed_process.stdout)
            except IOError as e:
                print(f"An error occurred while writing to {target_path}: {e}")


def main():
    parser = argparse.ArgumentParser(description='process the data')
    parser.add_argument('folder_path', type=str, help='The path to the folder containing data')
    parser.add_argument('--clean', action='store_true', help='Clean the folder, removing everything except .bdd files')

    args = parser.parse_args()
    folder_path = args.folder_path

    if args.clean:
        clean_folder_except_bdd(args.folder_path)
    else:
        escape_files_in_folder(folder_path)
        get_ast(folder_path)


if __name__ == "__main__":
    main()

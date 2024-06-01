from dataclasses import dataclass
from typing import List
import pyperclip

@dataclass
class Line:
    attempt: int
    line_number: int
    content: str
    error_types: List[dict]

def parse_markdown(file_path):
    # Read the markdown file

    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Parse each section into Line instances
    parsed_lines = []
    current_line = {}

    current_attempt = None
    current_line_number = 0
    current_content = ''
    current_error_types = []

    for line in lines:
        line = line.strip()
        
        if line.startswith('##'):
            current_attempt = int(line.split(' ')[1].rsplit('.')[0])

        if line.startswith('**Line Number**'):
            # Capture the line number
            current_line_number = int(line.split(': ')[1])

        if line.startswith('* **Line**'):
            # Capture the content
            current_content = line.split(': `')[1].rstrip('`')
        if line.startswith('* **Error Type**'):
            # Capture the error type and prepare for the next record
            error_types = line.split(': ')[1].split('; ')
            for error in error_types:
                if ' - ' not in error:
                    err = {
                        'error_type': error.strip()
                    }
                else:
                    try:
                        error_type, error_reason = error.split(' - ')
                        err = {
                            'error_type': error_type.strip(),
                            'error_reason': error_reason.strip()
                        }
                        current_error_types.append(err)
                    except ValueError:
                        print(f'[ERROR] Error in splitting error type and reason, see line {current_line_number} in attempt {current_attempt}')


        if current_line_number and current_attempt and current_content and current_error_types:
            # Create a Line instance and reset the current values
            parsed_lines.append(Line(attempt=current_attempt, line_number=current_line_number, content=current_content, error_types=current_error_types))
            current_line_number = None
            current_content = None
            current_error_types = []
    
    # Add the last line if present
    if current_line:
        parsed_lines.append(Line(**current_line))

    return parsed_lines


ERRORS = {
    "Model": [
        "No model definition",
        "Invalid symbols in model name",
        "Encapsulating the model in brackets"
    ],
    "Entity": [
        "Incorrect sequence of entity attributes",
        "Invalid entity definition",
        "Lack of delineation among entity attributes",
        "Spaces in property definition",
        "Invalid character in action definition",
        "Invalid use of preposition in action definition",
        "Invalid use of preposition in state definition",
        "Use restricted keywords in state definition"
    ],
    "Scenario": [
        "Missing entity identifier",
        "Invalid sentence structure",
        "Lack of interactive statements",
        "Lack of domain statements",
        "Invalid domain statements",
        "Use action on property instead of entity",
        "Spaces in state reference",
        "Check if Entity is in another entity",
        "Use restricted keywords in Scenario name",
        "Referencing undefined property",
        "Referencing undefined state",
        "Referencing undefined action",
        "Referencing undefined entity",
        "Chaining properties",
        "Chaining entity identifiers",
        "Chaining entities",
        "Use made-up keywords",
        "Missing keyword",
        "Invalid symbol in property reference",
        "Invalid action reference",
        "Invalid property reference",
        "Setting an entity to a value instead of a state",
        "Invalid symbol in statement"
    ],
    "General": [
        "Division into multiple code blocks"
    ]
}

def find_unknown_errors(parsed_lines):
    known_errors = set()
    for category_errors in ERRORS.values():
        known_errors.update(category_errors)

    unknown_errors = set()

    for line in parsed_lines:
        for error in line.error_types:
            error_type = error['error_type']
            if error_type not in known_errors:
                unknown_errors.add(error_type + " in line " + str(line.line_number) + " in attempt " + str(line.attempt))

    if unknown_errors:
        print("Unknown Errors Found:")
        for error in unknown_errors:
            print(error)
    else:
        print("No unknown errors found.")


def get_longest_id_length():
    """e.g. E1.1 = 4, E1.10 = 5"""
    longest_id = max(len(section) for section in ERRORS.values())
    longest_section_id = len(ERRORS)
    return len(f'E{str(longest_section_id)}.{str(longest_id)}')


def get_longest_error_description_length():
    longest_description = max(len(error) for section in ERRORS.values() for error in section)
    return longest_description


LONGEST_ID_LENGTH = get_longest_id_length()
LONGEST_DESCRIPTION_LENGTH = get_longest_error_description_length()


def get_number_of_specific_errors(error_type, parsed_data) -> dict[int, int]:
    # check how many times the current error type is present in the attempt
    amount = {}
    for data in parsed_data:
        if data.attempt not in amount:
            amount[data.attempt] = 0
        for error in data.error_types:
            if error['error_type'] == error_type:
                amount[data.attempt] += 1
                
    return amount


def generate_attempt_data(error_type, parsed_data) -> str: 
    error = get_number_of_specific_errors(error_type, parsed_data)

    text = " & " + " & ".join([' '.ljust(2) if error.get(i, 0) == 0 else str(error.get(i, 0)).ljust(2) for i in range(1, 11)]) + " & "
    total = rf'\gc{{{len([val for val in error.values() if val != 0]) * 10}}}'

    return text + total + r' \\'

def generate_latex_table_with_id(parsed_data):
    latex_content = []

    # LaTeX header and setup for the table
    latex_content.append(r'\begin{table}[!htbp]')
    latex_content.append(r'    \centering')
    latex_content.append(r'    \makebox[\linewidth]{')
    latex_content.append(r'    \begin{tabular}{l l*{10}{c} r}')
    latex_content.append(r'        \multirow{2}{*}{\thead{ID}} & \multirow{2}{*}{\thead{Type of Error}} & \multicolumn{10}{c}{\textbf{Attempt}} & \multirow{2}{*}{\thead{Total}} \\')
    latex_content.append(r'        \cmidrule(lr){3-12}')
    latex_content.append(r'             &                                                  & 1  & 2  & 3  & 4  & 5  & 6  & 7  & 8  & 9  & 10 & \\')
    latex_content.append(r'        \midrule')

    for i, section in enumerate(ERRORS.items()):
        section_id = i+1
        latex_content.append(rf'        \textbf{{E{section_id}}} & \textbf{{{section[0]}}}\\')
        for j, error_type in enumerate(section[1]):
            error_id = f'E{section_id}.{j+1}'
            formatted_error_id = error_id.ljust(LONGEST_ID_LENGTH)
            formatted_error_type = error_type.ljust(LONGEST_DESCRIPTION_LENGTH)
            error_id_and_type = rf'        {formatted_error_id} & {formatted_error_type}'
            error_values = generate_attempt_data(error_type, parsed_data)
            latex_content.append(error_id_and_type + error_values)
        latex_content.append(r'')

    latex_content.append(r'    \end{tabular}')
    latex_content.append(r'    }')
    latex_content.append(r'    \caption{<Caption>}')
    latex_content.append(r'    \label{tab:<name>}')
    latex_content.append(r'\end{table}')
    
    return '\n'.join(latex_content)

def generate_latex_table(parsed_data):
    latex_content = []

    # LaTeX header and setup for the table
    latex_content.append(r'\begin{table}[!htbp]')
    latex_content.append(r'    \centering')
    latex_content.append(r'    \makebox[\linewidth]{')
    latex_content.append(r'    \begin{tabular}{l*{10}{c} r}')
    latex_content.append(r'        \multirow{2}{*}{\thead{Type of Error}} & \multicolumn{10}{c}{\textbf{Occurrences / Attempt}} & \multirow{2}{*}{\thead{Total}} \\')
    latex_content.append(r'        \cmidrule(lr){2-11}')
    latex_content.append(LONGEST_DESCRIPTION_LENGTH * ' ' + '         & 1  & 2  & 3  & 4  & 5  & 6  & 7  & 8  & 9  & 10 & ' + r'\\')
    latex_content.append(r'        \midrule')

    for i, section in enumerate(ERRORS.items()):
        if i != 0:
            latex_content.append(rf'        \vspace{{-0.3cm}}\\')

        latex_content.append(rf'        \textbf{{{section[0]}}} \vspace{{0.15cm}}\\')
        for j, error_type in enumerate(section[1]):
            formatted_error_type = error_type.ljust(LONGEST_DESCRIPTION_LENGTH)
            error_id_and_type = rf'        {formatted_error_type}'
            error_values = generate_attempt_data(error_type, parsed_data)
            latex_content.append(error_id_and_type + error_values)
        latex_content.append(r'')

    latex_content.append(r'    \end{tabular}')
    latex_content.append(r'    }')
    latex_content.append(r'    \caption{<Caption>}')
    latex_content.append(r'    \label{tab:<name>}')
    latex_content.append(r'\end{table}')
    
    return '\n'.join(latex_content)

def main():
    # Path to the markdown file
    file_path = './generated/v1/data.md'
    parsed_data = parse_markdown(file_path)
    latex_table = generate_latex_table(parsed_data)
    pyperclip.copy(latex_table)

    print(latex_table)

    print("---")
    print("Table copied to clipboard.")
    print("---")

    find_unknown_errors(parsed_data)


if __name__ == '__main__':
    main()

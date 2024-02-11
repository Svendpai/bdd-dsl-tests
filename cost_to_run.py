import json
import tiktoken
from typing import Dict, Any


GPT3_5_INPUT_COST_PER_TOKEN = 0.0005 / 1000
GPT3_5_OUTPUT_COST_PER_TOKEN = 0.0015 / 1000
GPT4_INPUT_COST_PER_TOKEN = 0.01 / 1000
GPT4_OUTPUT_COST_PER_TOKEN = 0.03 / 1000
ESTIMATED_OUTPUT_TOKENS = 2000
REPLICATIONS = 5
DATASET_PATH = "./BDD_DSL_dataset.json"
PROMPT_PATH = "./prompt.txt"
ENCODING = tiktoken.get_encoding("cl100k_base")


def load_json_file(file_path: str) -> Dict[str, Any]:
    """Load a JSON file and return its content."""
    with open(file_path, "r", encoding="utf-8") as json_file:
        return json.load(json_file)


def load_instruction_prompt(file_path: str) -> str:
    """Load a text file and return its content as a string."""
    with open(file_path, "r", encoding="utf-8") as prompt_file:
        return prompt_file.read()


def get_token_count(text: str) -> int:
    """Return the token count of the given text using the predefined encoding."""
    return len(ENCODING.encode(text))


def calculate_costs(input_tokens: int, output_tokens: int, input_cost_per_token: float, output_cost_per_token: float) -> float:
    """Calculate the cost of running a model based on input and output token counts."""
    return (input_tokens * input_cost_per_token) + (output_tokens * output_cost_per_token) * REPLICATIONS


def main():
    data = load_json_file(DATASET_PATH)
    instruction_prompt = load_instruction_prompt(PROMPT_PATH)
    instruction_token_count = get_token_count(instruction_prompt)

    input_token_count = sum(get_token_count(
        entry["prompt"]) + instruction_token_count for entry in data["tasks"])
    estimated_output_token_count = len(
        data["tasks"]) * ESTIMATED_OUTPUT_TOKENS

    print(f"Instruction Token Count: {instruction_token_count}")
    print(f"Prompt Token Count: {input_token_count}")

    cost_gpt_3_5 = calculate_costs(input_token_count, estimated_output_token_count,
                                   GPT3_5_INPUT_COST_PER_TOKEN, GPT3_5_OUTPUT_COST_PER_TOKEN)
    cost_gpt_4 = calculate_costs(input_token_count, estimated_output_token_count,
                                 GPT4_INPUT_COST_PER_TOKEN, GPT4_OUTPUT_COST_PER_TOKEN)

    print(f"Cost to run GPT-3.5: ${cost_gpt_3_5:.2f}")
    print(f"Cost to run GPT-4: ${cost_gpt_4:.2f}")


if __name__ == "__main__":
    main()

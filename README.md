# Investigating Grammar Understanding in Large Language Models through Prompt Engineering

This repository is associated with my Master's thesis:

"Investigating Grammar Understanding in Large Language Models through Prompt Engineering"

## Overview

* `/base` contains the widgets model
* `/compiler` contains the DSL compiler and AST extractor
* `/generated` contains the LLM-generated code and data for this project
  * This includes prompts, responses, similarity measurements, and visualizations
* `/other` contains miscellaneous scripts and files that are not used in the final product
* `/possible_solutions` contains the hand-crafted ground truth examples
* `/quantitative_tests` contains the data for conducting the quantitative tests
* `calculate_metrics.py` is the script used to generate the similarity measurements and can be run from the command line
* `create_graphs.ipynb` is a Jupyter notebook used for visualizing the similarity measurements
* `generate_table.py` is used to translate the `data.md` files from the iterations to the latex tables seen in the paper

# Guide to Python fundamentals

This repository contains a structured set of practical exercises designed to learn and consolidate the basic concepts of Python programming. The modules cover everything from initial syntax and data structures to text processing, operating system operations, and structured file manipulation.

## What problem this repository solves

When learning to program in Python, students often face a disconnect between theory and real-world practice. This repository solves that problem by offering practical, sequential labs that cover:
- A gradual transition from basic concepts (variables, data types, conditionals, and loops) to more complex tasks (biological sequence processing, basic cryptography, and systems administration).
- Handling structured data such as CSV and JSON files using Python's native libraries.
- Executing operating system commands programmatically, preparing developers for automation and DevOps tasks.

## Technologies used

The project is based on the following tools and technologies:
- Python 3 as the primary programming language.
- Python standard libraries, including:
  - `re` for regular expression manipulation and text cleaning.
  - `json` for processing and handling JSON formatted data.
  - `os` and `subprocess` to interact with the operating system and execute processes.
- AWS Cloud9 as the cloud-based integrated development environment.

## Use of AWS Cloud9 in this project

This project is configured to be developed and executed using AWS Cloud9. AWS Cloud9 is a cloud-based integrated development environment (IDE) that lets you write, run, and debug code with just a web browser.

The repository includes the `.c9` folder, which contains environment-specific settings to make running the scripts easier without needing complex local dependency setup.

To run the scripts within AWS Cloud9, you can use the integrated terminal of the associated Linux instance or use the run button in the IDE graphical interface. This ensures that all developers share a consistent environment, eliminating operating system compatibility issues.

## Specific use cases and when to use this repository

This repository is useful in the following situations:
- Guided Python learning for beginners looking for commented and applied code examples.
- Practical text processing and basic bioinformatics, such as extracting substrings and calculating molecular properties of sequences like insulin.
- Implementing classic cryptography algorithms at an introductory level, such as the Caesar cipher.
- Basic automation of operating system tasks through systems administration scripts.

## File structure and exercise description

The purpose of each file in the repository is detailed below:
- `01-hello-world.py`: Introduction to basic syntax and printing messages to the console.
- `02-numeric-data.py`: Working with numeric data types (integers, floats, and complex numbers).
- `03-string-data-type.py`: Character string manipulation and concatenation.
- `04-collections.py`: Introduction to lists, tuples, and dictionaries.
- `05-categorize-values.py`: Categorizing different data types inside mixed collections.
- `06-composite-data.py`: Creating and handling composite structures using files like `car_fleet.csv`.
- `07-workWithConditionals.py`: Flow control using basic conditionals.
- `07.1-validador-de-datos.py`: Practical example of conditional logic validating age and budget.
- `08-while-loop.py`: Using loops controlled by conditions.
- `08.1-for-loop.py`: Using loops with a defined count.
- `10-analyze-insulin.py`: Processing and cleaning DNA/protein sequences using regular expressions.
- `11-string-insulin.py`: Analyzing sequences applied to molecular calculation.
- `12-net-charge.py`: Calculating the net charge of insulin across different pH levels using loops and dictionaries.
- `13-caesar-cipher.py`: Implementing Caesar cipher encryption and decryption with custom functions.
- `14.1-calc_weight_json.py`: Main script that calculates the molecular weight of insulin by importing a custom module.
- `jsonFileHandler.py`: Auxiliary module for safe JSON file reading with error handling.
- `sys-admin.py`: Operating system interaction to run commands and list active processes.
- `debugCipher1.py` to `debugCipher4.py`: Exercises designed to learn how to debug errors in Caesar cipher implementations.
- `car_fleet.csv`: CSV data file used in the composite data exercise.
- `files/insulin.json`: File containing structured molecule and molecular weight data.

## How to run the repository scripts

1. Open your AWS Cloud9 environment.
2. Clone this repository or navigate to the directory where the project is located.
3. To run any Python file, use the following command in the integrated terminal:
   ```bash
   python3 filename.py
   ```
   For example, for the molecular calculation case:
   ```bash
   python3 14.1-calc_weight_json.py
   ```

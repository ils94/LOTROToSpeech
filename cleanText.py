# This file only exist, so I can clean the most common misread from Tesseract due LOTRO font.

import re
import os
import globalVariables


def clear(text):
    text = text.replace('\n', ' ')

    text = replace_strings(text)

    text_without_double_spaces = re.sub(r'\s+', ' ', text)

    return re.sub(r'[^a-zA-Z0-9!?.;,:\-\'\"äöüßàâçéèêëîïôûùÿæœÀÂÇÉÈÊËÎÏÔÛÙÜŸÆŒ ]', '', text_without_double_spaces)


def create_replace_string_file():
    if not os.path.exists(globalVariables.config_path):
        os.makedirs(globalVariables.config_path)

    try:
        with open(globalVariables.config_path + r"/replace_string.txt", "x") as file:
            pass  # This creates an empty file if it doesn't exist
    except FileExistsError:
        pass  # File already exists, no need to create it


def replace_strings(input_string):
    create_replace_string_file()

    file_path = globalVariables.config_path + r"/replace_string.txt"

    # Read the file and store its contents in a dictionary.
    replacements = {}
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 2:
                old_str, new_str = parts[0], parts[1]
                # If new_str is "", consider it as an empty string.
                if new_str == '""':
                    new_str = ''
                replacements[old_str] = new_str

    # Perform replacements on the input string.
    for old_str, new_str in replacements.items():
        input_string = input_string.replace(old_str, new_str)

    return input_string

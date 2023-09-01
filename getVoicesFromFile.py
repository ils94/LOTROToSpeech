import random
import os
import globalVariables

male_voice_file_path = globalVariables.voices_path + r"/Male Voices.txt"
female_voice_file_path = globalVariables.voices_path + r"/Female Voices.txt"


def get_voice(file_path):
    create_voices_path_files()

    # Initialize an empty list to store lines from the file
    lines = []

    if "Male" in file_path:
        if not os.path.getsize(male_voice_file_path) == 0:
            file_path = male_voice_file_path
    else:
        if not os.path.getsize(female_voice_file_path) == 0:
            file_path = female_voice_file_path

    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            # Read each line from the file and split by "\n"
            for line in file:
                lines.extend(line.strip().split('\n'))

        # Check if there are any lines in the list
        if lines:
            # Randomly select and return one element from the list
            random_element = random.choice(lines)
            return random_element
        else:
            return ""

    except FileNotFoundError:
        return ""


def create_voices_path_files():
    if not os.path.exists(globalVariables.voices_path):
        os.makedirs(globalVariables.voices_path)

    try:
        with open(globalVariables.voices_path + r"/Female Voices.txt", "x") as file:
            pass  # This creates an empty file if it doesn't exist
        with open(globalVariables.voices_path + r"/Male Voices.txt", "x") as file:
            pass  # This creates an empty file if it doesn't exist
    except FileExistsError:
        pass  # File already exists, no need to create it

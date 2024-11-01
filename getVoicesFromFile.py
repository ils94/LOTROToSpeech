import random
import os
import globalVariables

male_voice_file_path = globalVariables.voices_path + r"/Male Voices.txt"
female_voice_file_path = globalVariables.voices_path + r"/Female Voices.txt"


def get_voice(file_path):
    create_voices_path_files()

    lines = []

    if "Male" in file_path:
        if not os.path.getsize(male_voice_file_path) == 0:
            file_path = male_voice_file_path
    else:
        if not os.path.getsize(female_voice_file_path) == 0:
            file_path = female_voice_file_path

    try:
        with open(file_path, 'r') as file:
            for line in file:
                lines.extend(line.strip().split('\n'))

        if lines:
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
            pass
        with open(globalVariables.voices_path + r"/Male Voices.txt", "x") as file:
            pass
    except FileExistsError:
        pass

import random


def get_voice(file_path):
    # Initialize an empty list to store lines from the file
    lines = []

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

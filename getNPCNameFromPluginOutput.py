import os
from pathlib import Path
import getNPCGender

file_path = str(Path.home() / 'Documents') + r"/The Lord of the Rings Online/Script.log"


def get_npc_gender_by_name():
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()

                if lines:
                    last_line = lines[-1].strip()
                    return getNPCGender.return_npc_gender(last_line), last_line
                else:
                    print(f"The file {file_path} is empty.")
                    return "", ""
        except Exception as e:
            print(f"Error reading the file: {e}")
            return "", ""
    else:
        print(f"The file {file_path} does not exist.")
        return "", ""

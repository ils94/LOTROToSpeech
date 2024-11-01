import json
import globalVariables
import os


def create_npcs_voices_file():
    if not os.path.exists(globalVariables.config_path):
        os.makedirs(globalVariables.config_path)

    file_path = os.path.join(globalVariables.config_path, "npcs_voices.json")

    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            json.dump([], file)


def add_info_to_json(new_data):
    create_npcs_voices_file()

    try:
        file_path = os.path.join(globalVariables.config_path, "npcs_voices.json")
        with open(file_path, 'r') as file:
            existing_data = json.load(file)

        if new_data not in existing_data:
            existing_data.append(new_data)

            with open(file_path, 'w') as file:
                json.dump(existing_data, file, indent=4)
        else:
            pass
    except Exception:
        pass


def get_voice_by_name(name):
    create_npcs_voices_file()

    try:
        file_path = os.path.join(globalVariables.config_path, "npcs_voices.json")
        with open(file_path, 'r') as file:
            existing_data = json.load(file)

        for item in existing_data:
            if 'Name' in item and item['Name'] == name:
                return item.get('Voice', 'Voice not found')
        return ""
    except Exception:
        return ""

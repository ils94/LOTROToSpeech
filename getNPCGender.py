file_path = "Resources/NPCs/npcs.txt"


def find_npc_in_the_file(file_path, search_string, encoding="utf-8"):
    try:
        with open(file_path, "r", encoding=encoding) as file:
            file_contents = file.read().split("\n")

        search_string = search_string.lower()

        for line in file_contents:
            if search_string in line.lower():
                return line

        return None
    except UnicodeDecodeError:
        print(f"Unable to decode the file using {encoding} encoding.")
        return None


def return_npc_gender(search_string):
    result = find_npc_in_the_file(file_path, search_string)

    if result is not None:
        result_lower = result.lower()
        if "[m]" in result_lower:
            return "male"
        if "[f]" in result_lower:
            return "female"

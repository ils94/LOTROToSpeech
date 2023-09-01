file_path = "Resources/NPCs/npcs.txt"


def find_npc_in_the_file(file_path, search_string, encoding="utf-8"):
    try:
        with open(file_path, "r", encoding=encoding) as file:
            file_contents = file.read().split("\n")

        # Convert the search string to lowercase for case-insensitive search
        search_string = search_string.lower()

        # Iterate through the file contents to find the element containing the search string
        for line in file_contents:
            # Convert each line to lowercase for case-insensitive comparison
            if search_string in line.lower():
                return line

        # If the search string was not found in any element, return None
        return None
    except UnicodeDecodeError:
        print(f"Unable to decode the file using {encoding} encoding.")
        return None


def return_npc_gender(search_string):
    result = find_npc_in_the_file(file_path, search_string)

    if result is not None:
        result_lower = result.lower()  # Convert the result to lowercase
        if "[m]" in result_lower:
            return "male"
        if "[f]" in result_lower:
            return "female"

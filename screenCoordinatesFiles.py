import os
import globalVariables


def save_coordinates(cor_x, cor_y, e_x, e_y):
    if not os.path.exists(globalVariables.coordinates_path):
        os.makedirs(globalVariables.coordinates_path)

    with open(globalVariables.coordinates_path + r"/coordinates.txt", "w") as file:
        file.write(f"Start X: {cor_x}\n")
        file.write(f"Start Y: {cor_y}\n")
        file.write(f"End X: {e_x}\n")
        file.write(f"End Y: {e_y}\n")


def load_coordinates():
    try:
        with open(globalVariables.coordinates_path + r"/coordinates.txt", "r") as file:
            lines = file.readlines()
            cor_x = float(lines[0].split(":")[1].strip())
            cor_y = float(lines[1].split(":")[1].strip())
            e_x = float(lines[2].split(":")[1].strip())
            e_y = float(lines[3].split(":")[1].strip())

            return cor_x, cor_y, e_x, e_y
    except FileNotFoundError:
        return None, None, None, None

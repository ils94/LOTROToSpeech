import sys
from tkinter import messagebox
import os
import pytesseract

import globalVariables

app_data_path = fr'C:\Users\{os.getlogin()}\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

program_files_path = fr'C:\Program Files\Tesseract-OCR\tesseract.exe'


def create_tesseract_path_file():

    if not os.path.exists(globalVariables.config_path):
        os.makedirs(globalVariables.config_path)

    try:
        with open(globalVariables.config_path + r"/tesseract_path.txt", "x") as file:
            pass  # This creates an empty file if it doesn't exist
    except FileExistsError:
        pass  # File already exists, no need to create it


def load_tesseract_path():
    path = globalVariables.config_path

    try:
        with open("tesseract_path.txt", "r") as file:
            lines = file.readlines()

            if len(lines) > 0:
                path = lines[0].strip()  # Use strip() to remove leading/trailing whitespace

            return path
    except FileNotFoundError:
        return ""


def look_for_tesseract():

    create_tesseract_path_file()

    load_tesseract_path()

    if os.path.exists(app_data_path):
        pytesseract.pytesseract.tesseract_cmd = app_data_path
    elif os.path.exists(program_files_path):
        pytesseract.pytesseract.tesseract_cmd = program_files_path
    else:
        path = load_tesseract_path()

        if path:
            if r"\tesseract.exe" not in path:
                pytesseract.pytesseract.tesseract_cmd = load_tesseract_path() + r"\tesseract.exe"
            else:
                pytesseract.pytesseract.tesseract_cmd = load_tesseract_path()
        else:
            messagebox.showerror("Error", "Cannot find Tesseract. Download Tesseract from LOTRO To Speech "
                                          "Github page and install it. If you have already installed it, but installed "
                                          "in another path, go to LTSET root folder, and paste the path to your "
                                          "Tesseract into tesseract_path.txt.")

            sys.exit()

import tkinter as tk
import sys
from tkinter import messagebox, Menu
from PIL import ImageGrab
import pytesseract
import threading
import os
import time
from elevenlabs import generate, set_api_key, save
import cv2
import numpy as np
import pyautogui
import keyboard
import re
from playsound import playsound
from plyer import notification

rect_color = "#ffcccb"

app_data_path = fr'C:\Users\{os.getlogin()}\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

program_files_path = fr'C:\Program Files\Tesseract-OCR\tesseract.exe'


def look_for_tesseract():
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


def create_tesseract_path_file():
    try:
        with open("tesseract_path.txt", "x") as file:
            pass  # This creates an empty file if it doesn't exist
    except FileExistsError:
        pass  # File already exists, no need to create it


def load_tesseract_path():
    path = ""

    try:
        with open("tesseract_path.txt", "r") as file:
            lines = file.readlines()

            if len(lines) > 0:
                path = lines[0].strip()  # Use strip() to remove leading/trailing whitespace

            return path
    except FileNotFoundError:
        return ""


def tts_engine(text):
    global already_talked

    if not os.path.exists("audios"):
        # If it doesn't exist, create it
        os.makedirs("audios")

    words = text.split()

    # Take the first 5 words
    first_5_words = "".join(words[:5]).lower()

    first_5_words = re.sub(r'[^a-zA-Z0-9]', '', first_5_words)

    audio_file = "audios/" + first_5_words + ".mp3"

    key, voice = load_api_key()

    if already_talked:
        return

    if os.path.exists(audio_file):
        playsound(audio_file)
    else:
        if text:
            if key:
                try:
                    set_api_key(key)

                    if not voice:
                        voice = "Bella"

                    audio = generate(
                        text=text,
                        voice=voice,
                        model="eleven_monolingual_v1"
                    )

                    save(audio, audio_file)

                    playsound(audio_file)

                except Exception as e:
                    messagebox.showerror("Error", str(e))
            else:
                messagebox.showerror("Error", "No API Key.")
                time.sleep(3)

    already_talked = True


def create_api_key_file():
    try:
        with open("api_key.txt", "x") as file:
            pass  # This creates an empty file if it doesn't exist
    except FileExistsError:
        pass  # File already exists, no need to create it


def load_api_key():
    key, voice = "", ""

    try:
        with open("api_key.txt", "r") as file:
            lines = file.readlines()

            if len(lines) > 0:
                key = lines[0].strip()  # Use strip() to remove leading/trailing whitespace

            if len(lines) > 1:
                voice = lines[1].strip()  # Use strip() to remove leading/trailing whitespace

            return key, voice
    except FileNotFoundError:
        return "", ""


def save_coordinates(cor_x, cor_y, e_x, e_y):
    with open("coordinates.txt", "w") as file:
        file.write(f"Start X: {cor_x}\n")
        file.write(f"Start Y: {cor_y}\n")
        file.write(f"End X: {e_x}\n")
        file.write(f"End Y: {e_y}\n")


def load_coordinates():
    try:
        with open("coordinates.txt", "r") as file:
            lines = file.readlines()
            cor_x = float(lines[0].split(":")[1].strip())
            cor_y = float(lines[1].split(":")[1].strip())
            e_x = float(lines[2].split(":")[1].strip())
            e_y = float(lines[3].split(":")[1].strip())

            return cor_x, cor_y, e_x, e_y
    except FileNotFoundError:
        return None, None, None, None


def on_press(event):
    global start_x, start_y, rect

    if event.state & 0x4:
        start_x = canvas.canvasx(event.x)
        start_y = canvas.canvasy(event.y)

        if rect:
            canvas.delete(rect)
        rect = None


def on_drag(event):
    global rect
    cur_x = canvas.canvasx(event.x)
    cur_y = canvas.canvasy(event.y)

    if event.state & 0x4:
        if rect:
            canvas.coords(rect, start_x, start_y, cur_x, cur_y)
        else:
            rect = canvas.create_rectangle(start_x, start_y, cur_x, cur_y, fill=rect_color)


def on_release(event):
    global end_x, end_y

    if event.state & 0x4:
        end_x = canvas.canvasx(event.x)
        end_y = canvas.canvasy(event.y)

        save_coordinates(start_x, start_y, end_x, end_y)


def start_monitoring():
    monitor_thread = threading.Thread(target=monitor_loop)
    monitor_thread.setDaemon(True)
    monitor_thread.start()


def enable_disable_tts():
    global enable

    if enable:
        enable = False

        notification.notify(
            title="LOTRO To Speech",
            message="TTS is now Disabled"
            # Specify the duration (in seconds) the notification should be displayed
        )

    else:
        enable = True

        notification.notify(
            title="LOTRO To Speech",
            message="TTS is now Enable"
            # Specify the duration (in seconds) the notification should be displayed
        )


def is_image_on_screen():
    global already_talked

    image_to_detect_1 = cv2.imread("quest.png")
    image_to_detect_2 = cv2.imread("nextObjective.png")

    screenshot = pyautogui.screenshot()

    screenshot_np = np.array(screenshot)
    screenshot_cv = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

    result_1 = cv2.matchTemplate(screenshot_cv, image_to_detect_1, cv2.TM_CCOEFF_NORMED)
    min_val_1, max_val_1, min_loc_1, max_loc_1 = cv2.minMaxLoc(result_1)

    result_2 = cv2.matchTemplate(screenshot_cv, image_to_detect_2, cv2.TM_CCOEFF_NORMED)
    min_val_2, max_val_2, min_loc_2, max_loc_2 = cv2.minMaxLoc(result_2)

    if max_val_1 > 0.7 or max_val_2 > 0.7:
        return True
    else:
        already_talked = False


def center_window(window, min_width, min_height):
    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate the x and y coordinates for centering
    x = (screen_width - min_width) // 2
    y = (screen_height - min_height) // 2

    # Set the window's geometry to center it on the screen
    window.geometry(f"{min_width}x{min_height}+{x}+{y}")


def ocr_preview(event):
    global ocr_text_window, ocr_text_widget, text_ocr

    def get_ocr():
        # Clear existing text
        ocr_text_widget.config(state=tk.NORMAL)
        ocr_text_widget.delete(1.0, tk.END)
        ocr_text_widget.insert(tk.END, text_ocr)
        ocr_text_widget.config(state=tk.DISABLED)

    if ocr_text_window is None or not ocr_text_window.winfo_exists():
        ocr_text_window = tk.Toplevel(root)
        ocr_text_window.title("OCR Result")
        ocr_text_window.geometry("500x500")
        ocr_text_window.iconbitmap("lotrotospeech.ico")
        ocr_text_window.attributes("-topmost", True)

        # Create and pack the Text widget
        ocr_text_widget = tk.Text(ocr_text_window, wrap=tk.WORD)
        ocr_text_widget.pack(fill=tk.BOTH, expand=True)

        menu_bar = Menu(ocr_text_window)

        menu = Menu(menu_bar, tearoff=0)

        menu.add_command(label="Refresh OCR", command=get_ocr)

        menu_bar.add_cascade(label="Menu", menu=menu)

        ocr_text_window.config(menu=menu_bar)

        # Center the window on the screen with a minimum size
        center_window(ocr_text_window, 500, 500)  # Adjust the minimum size as needed
    else:
        # If the window exists, bring it to the top (optional)
        ocr_text_window.attributes("-topmost", True)

    # Clear existing text
    ocr_text_widget.config(state=tk.NORMAL)
    ocr_text_widget.delete(1.0, tk.END)
    ocr_text_widget.insert(tk.END, text_ocr)
    ocr_text_widget.config(state=tk.DISABLED)


def monitor_loop():
    global start_x, start_y, end_x, end_y, enable, text_ocr

    while True:
        try:
            if end_x < start_x:
                start_x, end_x = end_x, start_x
            if end_y < start_y:
                start_y, end_y = end_y, start_y

            if is_image_on_screen():
                screenshot = ImageGrab.grab(bbox=(start_x, start_y, end_x, end_y))
                text = pytesseract.image_to_string(screenshot)

                text = text.replace('\n', ' ')
                text = text.replace('This is a repeatable quest that you have previously completed.', '')

                text_without_double_spaces = re.sub(r'\s+', ' ', text)

                cleaned_text = re.sub(r'[^a-zA-Z0-9!?.;,:\-\'\" ]', '', text_without_double_spaces)

                text_ocr = cleaned_text

                if enable:
                    tts_engine(text_ocr)

            time.sleep(0.5)
        except Exception as e:
            print(e)
            time.sleep(3)
            continue


root = tk.Tk()
root.title("LOTRO To Speech - Elevenlab TTS Version")
root.attributes("-alpha", 0.5)
root.attributes("-topmost", True)
root.state("zoomed")
root.iconbitmap("lotrotospeech.ico")
root.bind("<Control-a>", ocr_preview)

canvas = tk.Canvas(root, cursor="cross")
canvas.pack(fill=tk.BOTH, expand=True)

rect = None
enable = False
text_ocr = ""
already_talked = False
ocr_text_window = None
ocr_text_widget = None
start_x, start_y, end_x, end_y = load_coordinates()

canvas.bind("<ButtonPress-1>", on_press)
canvas.bind("<B1-Motion>", on_drag)
canvas.bind("<ButtonRelease-1>", on_release)

keyboard.add_hotkey("ctrl+alt", enable_disable_tts)

if start_x:
    rect = canvas.create_rectangle(start_x, start_y, end_x, end_y, fill=rect_color)

create_tesseract_path_file()

look_for_tesseract()

create_api_key_file()

start_monitoring()

root.mainloop()

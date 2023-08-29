import tkinter as tk
from tkinter import messagebox
from PIL import ImageGrab
import pytesseract
import threading
import os
import time
from elevenlabs import generate, play, set_api_key
import cv2
import numpy as np
import pyautogui
import keyboard
import re

pytesseract.pytesseract.tesseract_cmd = fr'C:\Users\{os.getlogin()}\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'


def tts_engine(text):
    key, voice = load_api_key()

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

                play(audio)
            except Exception as e:
                messagebox.showerror("ERROR", str(e).upper())
        else:
            messagebox.showerror("ERROR", "NO API KEY.")
            time.sleep(3)


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
            rect = canvas.create_rectangle(start_x, start_y, cur_x, cur_y)


def on_release(event):
    global end_x, end_y, monitoring

    if event.state & 0x4:
        end_x = canvas.canvasx(event.x)
        end_y = canvas.canvasy(event.y)

        save_coordinates(start_x, start_y, end_x, end_y)

        if not monitoring:
            start_monitoring()


def start_monitoring():
    global monitoring

    if not monitoring:
        monitor_thread = threading.Thread(target=monitor_loop)
        monitor_thread.setDaemon(True)
        monitoring = True
        monitor_thread.start()


def is_image_on_screen():
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


def monitor_loop():
    global start_x, start_y, end_x, end_y

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

                cleaned_text = re.sub(r'[^\w\s.!?;,\']', '', text_without_double_spaces)

                print(cleaned_text)

                if not keyboard.is_pressed("Ctrl"):
                    tts_engine(cleaned_text)

            time.sleep(0.5)
        except Exception as e:
            print(e)
            time.sleep(3)
            continue


root = tk.Tk()
root.title("LOTRO to Speech - Elevenlab TTS")
root.attributes("-alpha", 0.5)
root.attributes("-topmost", True)
root.state("zoomed")
root.iconbitmap("lotrotospeech.ico")

canvas = tk.Canvas(root, cursor="cross")
canvas.pack(fill=tk.BOTH, expand=True)

rect = None
monitoring = False
start_x, start_y, end_x, end_y = load_coordinates()

canvas.bind("<ButtonPress-1>", on_press)
canvas.bind("<B1-Motion>", on_drag)
canvas.bind("<ButtonRelease-1>", on_release)

create_api_key_file()

if start_x:

    rect = canvas.create_rectangle(start_x, start_y, end_x, end_y)

    if not monitoring:
        start_monitoring()

root.mainloop()

import tkinter as tk
from PIL import ImageGrab
import pytesseract
import threading
import os
import time
import pyttsx3
import cv2
import numpy as np
import pyautogui

pytesseract.pytesseract.tesseract_cmd = fr'C:\Users\{os.getlogin()}\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 150)

for voice in voices:
    if "EN-US" in voice.id:
        engine.setProperty('voice', voice.id)


class RectangleDrawer:
    def __init__(self, root):
        self.root = root
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)  # Bind closing event
        self.canvas = tk.Canvas(root, cursor="cross")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.rect = None
        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None
        self.monitor_thread = None
        self.monitoring = False

        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)
        self.root.bind("<Escape>", self.stop_monitoring)  # Bind ESC key to stop monitoring

    def on_press(self, event):
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)
        if self.rect:
            self.canvas.delete(self.rect)
        self.rect = None

    def on_drag(self, event):
        cur_x = self.canvas.canvasx(event.x)
        cur_y = self.canvas.canvasy(event.y)

        if self.rect:
            self.canvas.coords(self.rect, self.start_x, self.start_y, cur_x, cur_y)
        else:
            self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, cur_x, cur_y)

    def on_release(self, event):
        self.end_x = self.canvas.canvasx(event.x)
        self.end_y = self.canvas.canvasy(event.y)

        # Start monitoring when the user finishes drawing the rectangle
        if not self.monitoring:
            self.start_monitoring()

    def start_monitoring(self):
        if not self.monitoring:
            self.monitor_thread = threading.Thread(target=self.monitor_loop)
            self.monitoring = True
            self.monitor_thread.start()

    def stop_monitoring(self, event=None):
        if self.monitoring:
            self.monitoring = False
            self.monitor_thread.join()

    def on_closing(self):
        self.stop_monitoring()
        self.root.destroy()

    def is_image_on_screen(self):
        # Load the image to detect
        image_to_detect = cv2.imread("quest.png")

        # Capture the screen
        screenshot = pyautogui.screenshot()

        # Convert the screenshot to an OpenCV format
        screenshot_np = np.array(screenshot)
        screenshot_cv = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

        # Use template matching to find the image on the screen
        result = cv2.matchTemplate(screenshot_cv, image_to_detect, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        # If a match is found above the threshold, return True
        if max_val > 0.7:
            return True

    def monitor_loop(self):
        while self.monitoring:
            if self.end_x < self.start_x:
                self.start_x, self.end_x = self.end_x, self.start_x  # Swap coordinates if end_x is less than start_x
            if self.end_y < self.start_y:
                self.start_y, self.end_y = self.end_y, self.start_y  # Swap coordinates if end_y is less than start_y

            screenshot = ImageGrab.grab(bbox=(self.start_x, self.start_y, self.end_x, self.end_y))
            text = pytesseract.image_to_string(screenshot)
            print("Text within the rectangle:")
            print(text)

            # by removing the spaces, it also remove pauses whenever there is a line breaker, which speeds up the text speech!
            text = text.replace('\n', ' ')

            if text and self.is_image_on_screen():
                # Convert text to speech and play it
                engine.say(text)
                engine.runAndWait()

            time.sleep(0.5)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("LOTRO to Speech")
    root.attributes("-alpha", 0.5)
    root.state('zoomed')
    app = RectangleDrawer(root)
    root.mainloop()

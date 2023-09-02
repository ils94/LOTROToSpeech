import tkinter as tk
from tkinter import Menu, messagebox
import time
import keyboard
import pygame
import startThreads
import globalVariables
import screenCoordinatesFiles
import lookForTesseract
import enableDisableTTS
import OCRDetectionAndCleanup
import elevenLabsTTSEngine
import createAllFilesAndDirectories

rect_color = "#ffcccb"

# Initialize Pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.stop()  # Stop the initial Pygame playback


def on_press(event):
    global rect

    if event.state & 0x4:
        globalVariables.start_x = canvas.canvasx(event.x)
        globalVariables.start_y = canvas.canvasy(event.y)

        if rect:
            canvas.delete(rect)
        rect = None


def on_drag(event):
    global rect

    cur_x = canvas.canvasx(event.x)
    cur_y = canvas.canvasy(event.y)

    if event.state & 0x4:
        if rect:
            canvas.coords(rect, globalVariables.start_x,
                          globalVariables.start_y,
                          cur_x,
                          cur_y)
        else:
            rect = canvas.create_rectangle(globalVariables.start_x,
                                           globalVariables.start_y,
                                           cur_x,
                                           cur_y,
                                           fill=rect_color)


def on_release(event):
    if event.state & 0x4:
        globalVariables.end_x = canvas.canvasx(event.x)
        globalVariables.end_y = canvas.canvasy(event.y)

        screenCoordinatesFiles.save_coordinates(globalVariables.start_x,
                                                globalVariables.start_y,
                                                globalVariables.end_x,
                                                globalVariables.end_y)


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
    global ocr_text_window, ocr_text_widget

    def get_ocr():
        # Clear existing text
        ocr_text_widget.delete(1.0, tk.END)
        ocr_text_widget.insert(tk.END, globalVariables.text_ocr)

    if ocr_text_window is None or not ocr_text_window.winfo_exists():
        ocr_text_window = tk.Toplevel(root)
        ocr_text_window.title("OCR Result")
        ocr_text_window.geometry("500x500")
        ocr_text_window.iconbitmap("Resources/lotrotospeech.ico")
        ocr_text_window.attributes("-topmost", True)

        # Create and pack the Text widget
        ocr_text_widget = tk.Text(ocr_text_window, wrap=tk.WORD)
        ocr_text_widget.pack(fill=tk.BOTH, expand=True)

        menu_bar = Menu(ocr_text_window)

        menu = Menu(menu_bar, tearoff=0)

        menu.add_command(label="Refresh OCR", command=get_ocr)

        menu.add_command(label="Generate Audio", command=lambda: startThreads.start_monitoring(
            lambda: manual_audio_generation(ocr_text_widget.get("1.0", "end-1c"))))

        menu_bar.add_cascade(label="Menu", menu=menu)

        ocr_text_window.config(menu=menu_bar)

        # Center the window on the screen with a minimum size
        center_window(ocr_text_window, 500, 500)  # Adjust the minimum size as needed
    else:
        # If the window exists, bring it to the top (optional)
        ocr_text_window.attributes("-topmost", True)


def monitor_loop():
    while True:
        try:
            if OCRDetectionAndCleanup.ocr_detection_and_cleaup():

                if globalVariables.enable_disable:
                    elevenLabsTTSEngine.tts_engine(globalVariables.text_ocr)

            time.sleep(0.5)
        except Exception as e:
            print(e)
            time.sleep(3)
            continue


def manual_audio_generation(text):
    try:
        elevenLabsTTSEngine.tts_engine(text)
    except Exception as e:
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("LOTRO To Speech - ElevenLabs TTS Version")
root.attributes("-alpha", 0.5)
root.attributes("-topmost", True)
root.state("zoomed")
root.iconbitmap("Resources/lotrotospeech.ico")
root.bind("<Control-a>", ocr_preview)

canvas = tk.Canvas(root, cursor="cross")
canvas.pack(fill=tk.BOTH, expand=True)

rect = None

ocr_text_window = None
ocr_text_widget = None

(globalVariables.start_x,
 globalVariables.start_y,
 globalVariables.end_x,
 globalVariables.end_y) = screenCoordinatesFiles.load_coordinates()

canvas.bind("<ButtonPress-1>", on_press)
canvas.bind("<B1-Motion>", on_drag)
canvas.bind("<ButtonRelease-1>", on_release)

keyboard.add_hotkey("ctrl+alt", enableDisableTTS.enable_disable_tts)

keyboard.add_hotkey("ctrl+shift", elevenLabsTTSEngine.stop_audio)

createAllFilesAndDirectories.create()

if globalVariables.start_x:
    rect = canvas.create_rectangle(globalVariables.start_x,
                                   globalVariables.start_y,
                                   globalVariables.end_x,
                                   globalVariables.end_y,
                                   fill=rect_color)

lookForTesseract.look_for_tesseract()

startThreads.start_monitoring(monitor_loop)

root.mainloop()

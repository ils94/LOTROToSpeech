import pygame
import os
import re
import globalVariables
from elevenlabs import generate, set_api_key, save
import time
from tkinter import messagebox


def stop_audio():
    pygame.mixer.music.stop()

    pygame.mixer.music.unload()


def play_audio(audio):
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)  # Adjust the playback speed as needed

    # Unload the audio to free up memory
    pygame.mixer.music.unload()


def tts_engine(text):
    create_api_key_file()

    if not os.path.exists(globalVariables.audio_path_string):
        # If it doesn't exist, create it
        os.makedirs(globalVariables.audio_path_string)

    words = text.split()

    # Take the first 5 words
    first_5_words = "".join(words[:5]).lower()

    first_5_words = re.sub(r'[^a-zA-Z0-9]', '', first_5_words)

    audio_file = globalVariables.audio_path_string + "/" + first_5_words + ".mp3"

    key, voice = load_api_key()

    if globalVariables.already_talked:
        return

    if os.path.exists(audio_file):
        play_audio(audio_file)
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

                    play_audio(audio_file)

                except Exception as e:
                    messagebox.showerror("Error", str(e))
            else:
                messagebox.showerror("Error", "No API Key.")
                time.sleep(3)

    globalVariables.already_talked = True


def create_api_key_file():
    if not os.path.exists(globalVariables.api_file_path):
        os.makedirs(globalVariables.api_file_path)

    try:
        with open(globalVariables.api_file_path + r"/api_key.txt", "x") as file:
            pass  # This creates an empty file if it doesn't exist
    except FileExistsError:
        pass  # File already exists, no need to create it


def load_api_key():
    key, voice = "", ""

    try:
        with open(globalVariables.api_file_path + r"/api_key.txt", "r") as file:
            lines = file.readlines()

            if len(lines) > 0:
                key = lines[0].strip()  # Use strip() to remove leading/trailing whitespace

            if len(lines) > 1:
                voice = lines[1].strip()  # Use strip() to remove leading/trailing whitespace

            return key, voice
    except FileNotFoundError:
        return "", ""

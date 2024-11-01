import pygame
import os
import re
import globalVariables
from elevenlabs import save
from elevenlabs.client import ElevenLabs
import time
from tkinter import messagebox
import setVoiceByGender


def stop_audio():
    pygame.mixer.music.stop()

    pygame.mixer.music.unload()


def play_audio(audio):
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()


def tts_engine(text):
    create_api_key_file()
    create_elevenlabs_model_file()

    if not os.path.exists(globalVariables.audio_path_string):
        os.makedirs(globalVariables.audio_path_string)

    words = text.split()

    first_5_words = "".join(words[:5]).lower()

    first_5_words = re.sub(r'[^a-zA-Z0-9]', '', first_5_words)

    audio_file = globalVariables.audio_path_string + "/" + first_5_words + ".mp3"

    key = load_api_key()

    model = load_elevenlabs_model()

    if globalVariables.already_talked:
        return

    if os.path.exists(audio_file):
        play_audio(audio_file)
    else:
        if text:
            if key:
                try:
                    client = ElevenLabs(
                        api_key=key,
                    )

                    voice = setVoiceByGender.set_voice("elevenlabs")

                    print(voice)

                    if model:
                        set_model = model
                    else:
                        set_model = "eleven_turbo_v2_5"

                    audio = client.generate(
                        text=text,
                        voice=voice,
                        model=set_model
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
    if not os.path.exists(globalVariables.config_path):
        os.makedirs(globalVariables.config_path)

    try:
        with open(globalVariables.config_path + r"/api_key.txt", "x") as file:
            pass
    except FileExistsError:
        pass


def load_api_key():
    key = ""

    try:
        with open(globalVariables.config_path + r"/api_key.txt", "r") as file:
            lines = file.readlines()

            if len(lines) > 0:
                key = lines[0].strip()

            return key
    except FileNotFoundError:
        return ""


def create_elevenlabs_model_file():
    if not os.path.exists(globalVariables.config_path):
        os.makedirs(globalVariables.config_path)

    try:
        with open(globalVariables.config_path + r"/elevenlabs_model.txt", "x") as file:
            pass
    except FileExistsError:
        pass


def load_elevenlabs_model():
    model = ""

    try:
        with open(globalVariables.config_path + r"/elevenlabs_model.txt", "r") as file:
            lines = file.readlines()

            if len(lines) > 0:
                model = lines[0].strip()

            return model
    except FileNotFoundError:
        return ""

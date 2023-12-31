import pygame
import os
import edge_tts
import re
import globalVariables
import setVoiceByGender
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


async def tts_engine(text) -> None:
    if not os.path.exists(globalVariables.audio_path_string):
        os.makedirs(globalVariables.audio_path_string)

    words = text.split()
    first_5_words = "".join(words[:5]).lower()
    first_5_words = re.sub(r'[^a-zA-Z0-9]', '', first_5_words)
    audio_file = globalVariables.audio_path_string + "/" + first_5_words + ".mp3"

    if globalVariables.already_talked:
        return

    if os.path.exists(audio_file):
        play_audio(audio_file)
    else:
        if text:
            try:
                voice = setVoiceByGender.set_voice("edge-tts")

                print(voice)

                communicate = edge_tts.Communicate(text, voice)

                await communicate.save(audio_file)

                play_audio(audio_file)
            except Exception as e:
                messagebox.showerror("Error", str(e))

    globalVariables.already_talked = True

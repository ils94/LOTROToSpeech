import pygame
import os
import edge_tts
import re
import globalVariables
import getNPCNameFromPluginOutput


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
    create_voice_file()

    if not os.path.exists(globalVariables.audio_path_string):
        os.makedirs(globalVariables.audio_path_string)

    words = text.split()
    first_5_words = "".join(words[:5]).lower()
    first_5_words = re.sub(r'[^a-zA-Z0-9]', '', first_5_words)
    audio_file = globalVariables.audio_path_string + "/" + first_5_words + ".mp3"

    # voice = load_voice_file()

    if globalVariables.already_talked:
        return

    if os.path.exists(audio_file):
        play_audio(audio_file)
    else:
        if text:
            # if not voice:
            #     voice = "en-GB-RyanNeural"

            gender = getNPCNameFromPluginOutput.get_npc_gender_by_name()

            voice = ""

            if gender == "male":
                voice = "en-US-ChristopherNeural"
            elif gender == "female":
                voice = "en-GB-SoniaNeural"

            communicate = edge_tts.Communicate(text, voice)

            await communicate.save(audio_file)

            play_audio(audio_file)

    globalVariables.already_talked = True


def create_voice_file():

    if not os.path.exists(globalVariables.config_path):
        os.makedirs(globalVariables.config_path)

    try:
        with open(globalVariables.config_path + r"/voice.txt", "x") as file:
            pass  # This creates an empty file if it doesn't exist
    except FileExistsError:
        pass  # File already exists, no need to create it


def load_voice_file():
    voice = ""

    try:
        with open(globalVariables.config_path + r"/voice.txt", "r") as file:
            lines = file.readlines()

            if len(lines) > 0:
                voice = lines[0].strip()  # Use strip() to remove leading/trailing whitespace

            return voice
    except FileNotFoundError:
        return ""

from pathlib import Path

already_talked = False
enable_disable = False

start_x = None
start_y = None
end_x = None
end_y = None

text_ocr = ""

tesseract_language = ""

elevenlabs_default_voice = None

audio_path_string = str(Path.home() / 'Documents') + r"/LOTROToSpeech/Audios"
config_path = str(Path.home() / 'Documents') + r"/LOTROToSpeech/Configs"
image_detection_path = str(Path.home() / 'Documents') + r"/LOTROToSpeech/Detection"
voices_path = str(Path.home() / 'Documents') + r"/LOTROToSpeech/Voices"

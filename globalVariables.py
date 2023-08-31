from pathlib import Path

already_talked = False
enable_disable = False

start_x = None
start_y = None
end_x = None
end_y = None

text_ocr = ""

audio_path_string = str(Path.home() / 'Documents') + r"/LOTROToSpeech/Audios"
tesseract_custom_path = str(Path.home() / 'Documents') + r"/LOTROToSpeech/Configs"
voices_path = str(Path.home() / 'Documents') + r"/LOTROToSpeech/Configs"
coordinates_path = str(Path.home() / 'Documents') + r"/LOTROToSpeech/Configs"
api_file_path = str(Path.home() / 'Documents') + r"/LOTROToSpeech/Configs"

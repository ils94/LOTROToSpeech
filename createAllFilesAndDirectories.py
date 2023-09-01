import elevenlabTTSEngine
import lookForTesseract
import retriveSaveNPCsVoices


# Just to make sure.

def create():
    elevenlabTTSEngine.create_elevenlabs_model_file()
    elevenlabTTSEngine.create_api_key_file()
    lookForTesseract.create_tesseract_lang_file()
    lookForTesseract.create_tesseract_path_file()
    retriveSaveNPCsVoices.create_npcs_voices_file()

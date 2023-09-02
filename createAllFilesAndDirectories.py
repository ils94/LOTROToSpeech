import elevenLabsTTSEngine
import lookForTesseract
import retriveSaveNPCsVoices
import getVoicesFromFile
import isQuestWindowOpen
import cleanText


# Just to make sure.

def create():
    elevenLabsTTSEngine.create_elevenlabs_model_file()
    elevenLabsTTSEngine.create_api_key_file()
    lookForTesseract.create_tesseract_lang_file()
    lookForTesseract.create_tesseract_path_file()
    retriveSaveNPCsVoices.create_npcs_voices_file()
    getVoicesFromFile.create_voices_path_files()
    isQuestWindowOpen.create_images_directory()
    cleanText.create_replace_string_file()

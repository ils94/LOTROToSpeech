import globalVariables


def default_voice():
    if globalVariables.tesseract_language == "deu":
        return "de-DE-KillianNeural"
    if globalVariables.tesseract_language == "fra":
        return "fr-FR-HenriNeural"
    else:
        return "en-US-ChristopherNeural"

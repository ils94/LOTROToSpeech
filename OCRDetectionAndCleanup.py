import globalVariables
import isQuestWindowOpen
import pytesseract
from PIL import ImageGrab
import lookForTesseract
import cleanText


def ocr_detection_and_cleaup():
    start_x = globalVariables.start_x
    start_y = globalVariables.start_y
    end_x = globalVariables.end_x
    end_y = globalVariables.end_y

    if end_x < start_x:
        start_x, end_x = end_x, start_x
    if end_y < start_y:
        start_y, end_y = end_y, start_y

    if isQuestWindowOpen.is_image_on_screen():
        screenshot = ImageGrab.grab(bbox=(start_x, start_y, end_x, end_y))

        globalVariables.tesseract_language = lookForTesseract.load_tesseract_lang()

        if not globalVariables.tesseract_language:
            globalVariables.tesseract_language = "eng"

        text = pytesseract.image_to_string(screenshot, lang=globalVariables.tesseract_language)

        globalVariables.text_ocr = cleanText.clear(text)

        return True

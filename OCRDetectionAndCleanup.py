import globalVariables
import isQuestWindowOpen
import pytesseract
from PIL import ImageGrab
import re
import lookForTesseract


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

        lang = lookForTesseract.load_tesseract_lang()

        if not lang:
            lang = "eng"

        config = '--oem 1 --dpi 300'

        text = pytesseract.image_to_string(screenshot, lang=lang, config=config)

        text = text.replace('\n', ' ')
        text = text.replace('This is a repeatable quest that you have previously completed.', '')

        text_without_double_spaces = re.sub(r'\s+', ' ', text)

        cleaned_text = re.sub(r'[^a-zA-Z0-9!?.;,:\-\'\" ]', '', text_without_double_spaces)

        globalVariables.text_ocr = cleaned_text

        return True

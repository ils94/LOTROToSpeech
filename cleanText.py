# This file only exist, so I can clean the most common misread from Tesseract due LOTRO font.

import re


def clear(text):
    text = text.replace('\n', ' ')
    text = text.replace('This is a repeatable quest that you have previously completed', '')
    text = text.replace('This is a repeatable quest that you have never completed', '')
    text = text.replace('Tl', "'I'll")
    text = text.replace("'T", "'I")

    text_without_double_spaces = re.sub(r'\s+', ' ', text)

    return re.sub(r'[^a-zA-Z0-9!?.;,:\-\'\" ]', '', text_without_double_spaces)

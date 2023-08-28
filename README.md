# LOTROToSpeech
Python program that uses Tesseract to do OCR to get text on your screen and convert to string.

# Installing

First, you will need to install Tesseract which is a program that converts image to string.

You can download Tesseract from this link:

https://github.com/UB-Mannheim/tesseract/wiki

After installing, you can run the script.

# Using the script

When you first run the script, a transparent window will appear, there, you will be able to drag a retangle where the text is (preferable where the quest text is in the quest window). The transparent window is just there so you can use the retangle, this was the easiest approach I found to be able to easily grab the screen coordinates. You can minimize the transparent window after that, but do not close it, the program needs to be on to perform the OCR.

# Notes

This script is still on it infancy, it still missing the part where the string is sent to an A.I to convert into audio.

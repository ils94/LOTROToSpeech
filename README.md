# LOTRO To Speech
Python program that uses Tesseract to perform OCR to detect text on your screen and convert it to string to be used on voice over A.Is

# Installing and using

First, you will need to install Tesseract which is a program that do OCR to convert image to text.

You can download Tesseract from this link:

https://github.com/UB-Mannheim/tesseract/wiki

After installing Tesseract download LTS (LOTRO To Speech - Windows TTS Version) or LTSEL (LOTRO To Speech - Eleven Labs TTS Version)

LTS download link: https://github.com/ils94/LOTROToSpeech/releases/download/release/LTS.zip

LTSEL download link: coming soon

unzip the version you downloaded, and run either LTS.exe or LTSEL.exe inside the root folder

# How to use

**LTS** (LOTRO To Speech - Windows TTS Version)

Open your game:

![enter image description here](https://github.com/ils94/LOTROToSpeech/blob/master/tutorial/tutorial1.PNG?raw=true)

Now open LOTRO To Speech overlay:

![enter image description here](https://github.com/ils94/LOTROToSpeech/blob/master/tutorial/tutorial2.PNG?raw=true)

Now hold CTRL and Mouse left button to drag a rectangle around the text of the quest:

![enter image description here](https://github.com/ils94/LOTROToSpeech/blob/master/tutorial/tutorial3.PNG?raw=true)

Tip: Resize the Quest Window as much as you can and leave the Quest Window to  the right of your screen, because if you leave it to your left, it may read your chat window.

After you are done setting everything, you can minimize it (do not close LOTRO to Speech)

----

**LTSEL** (LOTRO To Speech - Elevenlab TTS Version)

You will do the same setup as LTS, but, inside LTSEL folder, you will find an api_key.text (if it is not there, you can create api_key.txt file inside the root folder)

Open api_key.txt file and in the first line paste your API key from your Elevenlab account

If you want to change the voice over for LTSEL, you can put the voice name in the second line under your API Key.

Here is an example:

![enter image description here](https://github.com/ils94/LOTROToSpeech/blob/master/tutorial/tutorial4.PNG?raw=true)

If you do not add any voice name in the second line of api_key.txt, it will default the voice name to "Bella"

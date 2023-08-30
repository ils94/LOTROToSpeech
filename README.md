# LOTRO To Speech
Python program that uses Tesseract to perform OCR to detect text on your screen and convert it to string to be used on voice over A.Is

# Installing and using

First, you will need to install Tesseract which is a program that do OCR to convert image to text.

You can download Tesseract from this link:

https://github.com/UB-Mannheim/tesseract/wiki

After installing Tesseract, download LTSET (LOTRO To Speech - Edge-TTS Version) or LTSEL (LOTRO To Speech - Eleven Labs TTS Version)

LTSET download link: https://github.com/ils94/LOTROToSpeech/releases/download/LTSET-Release/LTSET.zip (up to date)

LTSEL download link: https://github.com/ils94/LOTROToSpeech/releases/download/LTSEL-Release/LTSEL.zip (outdated)

unzip the version you downloaded, and run either LTSET.exe or LTSEL.exe inside the root folder

# How to use

**LTSET** (LOTRO To Speech - Edge-TTS Version)

Open your game and look for a NPC with a quest available so you can use it as base:

![enter image description here](https://github.com/ils94/LOTROToSpeech/blob/master/tutorial/tutorial1.PNG?raw=true)

Now open LOTRO To Speech overlay and hold Ctrl + Left Mouse Button to drag a rectangle around the text of the quest:

![enter image description here](https://github.com/ils94/LOTROToSpeech/blob/master/tutorial/tutorial2.PNG?raw=true)

While in the LOTRO To Speech overlay, you can press Ctrl + A to open the OCR Result window, and test if the Quest Text is being captured well. Once you open the OCR Result Window, click out of it so the window loses focus, then, you can spam Ctrl + A to update it's text with the OCR Result. The OCR is performed every second, so give it time and keep adjusting the Rectangle around the text:

![enter image description here](https://github.com/ils94/LOTROToSpeech/blob/master/tutorial/tutorial3.PNG?raw=true)

Tip: Resize the Quest Window as much as you can and leave the Quest Window to  the right of your screen, because if you leave it to your left, it may read your chat window.

After you are done setting everything, you can minimize it (do not close LOTRO To Speech) and press "Ctrl+Alt" to enable the TTS.

You can change the voices for LTSET by opening the file (or creating the file) named "voice.txt" inside the root folder, and pasting in the first line one of the voices from those files:

[Edge-TTS Male EN-US Voices](https://github.com/ils94/LOTROToSpeech/blob/master/Languages%20for%20LTSET/Edge-TTS%20Male%20EN-US%20Voices.txt)

[Edge-TTS Female EN-US Voices](https://github.com/ils94/LOTROToSpeech/blob/master/Languages%20for%20LTSET/Edge-TTS%20Female%20EN-US%20Voices.txt)

Example:

![enter image description here](https://github.com/ils94/LOTROToSpeech/blob/master/tutorial/tutorial5.PNG?raw=true)

Leaving this file empty, will set "en-GB-RyanNeural" as default voice

----

**LTSEL** (LOTRO To Speech - Elevenlab TTS Version)

You will do the same setup as LTSET, but, inside LTSEL folder, you will find an api_key.text (if it is not there, you can create api_key.txt file inside the root folder)

Open api_key.txt file and in the first line paste your API key from your Elevenlab account

If you want to change the voice over for LTSEL, you can put the voice name in the second line under your API Key.

Here is an example:

![enter image description here](https://github.com/ils94/LOTROToSpeech/blob/master/tutorial/tutorial4.PNG?raw=true)

If you do not add any voice name in the second line of api_key.txt, it will default the voice name to "Bella"

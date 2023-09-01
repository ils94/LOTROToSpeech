# I want to say thanks to the people who helped immensely in this project

Lotro Companion for providing database files with the NPC names and their gender to make it possible to dynamically select voice models

dt192 for also helping me with database files and for also creating the plugin necessary to help make LOTRO To Speech more dynamic when selectin voice models.

You guys are more than awesome!

# LOTRO To Speech
A Python program that adds A.I voice over to Lord of The Rings Online quests by using OCR.

# Differences between LTSET and LTSEL

**LTSET** (LOTRO To Speech - Edge-TTS Version)

This version of LOTRO To Speech uses Edge-TTS (Microsoft Edge TTS) engine to generate audio files, this is one of the best and 100% free (for non comercial uses) A.I TTS available.

**LTSEL** (LOTRO To Speech - Elevenlab TTS Version)

If you are willing to fork some money for the best A.I audio generation in the market, this version is for you. It uses Elevenlab engine to generate audio files. More information below.

# Commands and Hotkeys

Holding Ctrl + Left Mouse Button while the LOTRO To Speech overlay is maximized, allows you to drag a rectangle that will be used to delimit the area where the OCR will be performed.

Ctrl + Alt = Enable/Disable TTS

Ctrl + Shift = Stop the Voice Over from playing

While the overlay is maximized, you can hit Ctrl + A to open the OCR Result Window to have a quick preview if the OCR is working.

In the OCR Result Window, you can quick refresh the Results by going into Menu - Refresh OCR.

If the OCR Result Window gets behind the LOTRO To Speech overlay, press Ctrl + A again to bring it back to the front.

# Installing

First, you will need to install Tesseract, which is a program that performs OCR to convert image to text.

You can download Tesseract from this link:

https://github.com/UB-Mannheim/tesseract/wiki

Then, I HIGHLY recommend you to download getNPCNames Plugin. This Plugin is VERY NECESSARY to dynamically choose the proper voice model to the NPCs based on their gender.

Link: [Thanking again dt192 for this plugin!](https://github.com/ils94/LOTROToSpeech/blob/master/Helpful%20Stuffs/Plugins/Dt192.zip)

After installing Tesseract, download LTSET (LOTRO To Speech - Edge-TTS Version) or LTSEL (LOTRO To Speech - Eleven Labs TTS Version)

[LTSET Download Link](https://github.com/ils94/LOTROToSpeech/releases/download/LTSET-Release/LTSET.zip) (up to date)

[LTSEL Download Link](https://github.com/ils94/LOTROToSpeech/releases/download/LTSEL-Release/LTSEL.zip) (up to date)

unzip the version you downloaded, and run either LTSET.exe or LTSEL.exe inside the program root folder.

# How to use (Outdated - Will make a new tutorial for the most recent version and more organized)

**LTSET** (LOTRO To Speech - Edge-TTS Version)

Open your game and look for a NPC with a quest available so you can use it as base:

![enter image description here](https://github.com/ils94/LOTROToSpeech/blob/master/tutorial/tutorial1.PNG?raw=true)

Now open LOTRO To Speech overlay and hold Ctrl + Left Mouse Button to drag a rectangle around the text of the quest:

![enter image description here](https://github.com/ils94/LOTROToSpeech/blob/master/tutorial/tutorial2.PNG?raw=true)

While in the LOTRO To Speech overlay, you can use the OCR Result Window by pressing Ctrl + A to quickly preview the OCR Result and see if the text is being captured.

![enter image description here](https://github.com/ils94/LOTROToSpeech/blob/master/tutorial/tutorial3.PNG?raw=true)

**Tip**: Resize the Quest Window as much as you can, and leave the Quest Window to  the right of your screen, because if you leave it to your left, it may read your chat window.

After you are done setting everything, you can minimize it (do not close LOTRO To Speech) and press "Ctrl + Alt" to enable the TTS.

You can change the voices for LTSET by opening the file (or creating the file) named "voice.txt" inside the program root folder, and paste in the first line one of the voices from those files:

[Edge-TTS Male EN-US Voices](https://github.com/ils94/LOTROToSpeech/blob/master/Languages%20for%20LTSET/Edge-TTS%20Male%20EN-US%20Voices.txt)

[Edge-TTS Female EN-US Voices](https://github.com/ils94/LOTROToSpeech/blob/master/Languages%20for%20LTSET/Edge-TTS%20Female%20EN-US%20Voices.txt)

Example:

![enter image description here](https://github.com/ils94/LOTROToSpeech/blob/master/tutorial/tutorial5.PNG?raw=true)

Leaving this file empty, will set "en-GB-RyanNeural" as default voice

----

**LTSEL** (LOTRO To Speech - Elevenlab TTS Version)

You will do the same setup as LTSET, but, inside LTSEL folder, you will find an api_key.text (if it is not there, you can create api_key.txt file inside the program root folder).

Open api_key.txt file and in the first line paste your API key from your Elevenlab account

If you want to change the voice over for LTSEL, you can put the voice name in the second line under your API Key.

Here is an example:

![enter image description here](https://github.com/ils94/LOTROToSpeech/blob/master/tutorial/tutorial4.PNG?raw=true)

If you do not add any voice name in the second line of api_key.txt, it will default the voice name to "Bella"

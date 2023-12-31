# Modding LOTRO To Speech

You can mod LOTRO To Speech. This is an important part because here you will learn how to put your prefered voice models, and add your own images to detect your Quest Window (very important if you use Interface Addons)

# Adding your voice models

You can add your voice models that are compatible with either Edge-TTS and ElevenLabs-TTS

Lets start with LTSET (LOTRO To Speech - Edge-TTS Version)

To add your voice models, you have to go to:

C:\Users\YOURUSER\Documents\LOTROToSpeech\Voices

There, you will find 2 files, Female Voices.txt and Male Voices.txt

When there is data in one of these files, LOTRO To Speech will understand that you want to use the voices on them, so it very important to only add the voice models compatible with **LTSET**, else, you will face an error when generating voice files.

You can take a look at the voice models available for Edge-TTS in this [link](https://github.com/ils94/LOTROToSpeech/blob/master/Helpful%20Stuffs/Languages/List%20of%20voices%20available%20in%20Edge%20TTS.txt)

I know it a lot information, but don't worry, i'll explain everything.

Lets take one of the voices from that link:

----

Name: Microsoft Server Speech Text to Speech Voice (en-AU, NatashaNeural)  
ShortName: en-AU-NatashaNeural  
Gender: Female  
Locale: en-AU  
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalities': ['Friendly', 'Positive']}  

----

Here we can see the name of the voice, it short name, the gender of the model, it locate (accent) and some other attributes in the VoiceTag.

The parameter that we need to put in the Female Voices.txt file is the **ShortName**

That will be: en-AU-NatashaNeural

By adding "en-AU-NatashaNeural" (no quotes) to the file, LOTRO To Speech will detect data in that and will load from this file instead.

If you want to add more voice models, just add the second, third and so on in the next line of the file:

en-AU-NatashaNeural  
en-CA-ClaraNeural  
en-HK-YanNeural  
 .  
 .  
 .  

For the LTSEL (LOTRO To Speech - ElevenLabs-TTS Version) the idea is the same, but of course, you will use voice models compatible with ElevenLabs:

Arnold  
Alex  
John  
.  
.  
.  

# Images used for detecting if Quest Window is open

If you use Interface Addons that change Quest Window appearence, well, LOTRO To Speech may not work, because it's default configuration is to look for vanilla sprites in the Quest Windows.

But don't worry! You can still use your Interface Addon, but you will need to feed LOTRO To Speech the knowledge of what it should look for to detect if the Quest Window is open in your Interface Addon.

For this, all you have to do is to take pictures of parts of your Quest Window. I recommend using Windows Snipping Tool.

With Snipping Tool, you can precisely take some image cues of your Quest Window like some unique button, text label, icon and so on.

After taking the picture(s), you should save them in:

C:\Users\YOURUSER\Documents\LOTROToSpeech\Detection

The formats supported for the detection images are: PNG, JPG and JPEG.

When LOTRO To Speech detect any of these files extensions in that directory, it will use them to do Pixel Recognition, instead of the default images in the LTS root folder.

# Other configurations

There are some other configurations that you can apply to LOTRO To Speech.

We will focus on 5 files here:

- api_key.txt
- elevenlabs_model.txt
- replace_string.txt
- tesseract_lang.txt
- tesseract_path.txt

---

**api_key.txt**

This file is where you put your ElevenLabs API key to generate voice files from their tool, if you are using LTSEL (LOTRO To Speech - ElevenLabs-TTS Version) you have to save your API Key in that file, else, you will receive an error when trying to generate voice files.

---

**elevenlabs_model.txt**

Here you can add voice models supported by ElevenLabs.

Currently, there are only 2 voice models supported:

- monolingual
- multilingual

For more information, visit [Models - ElevenLabs](https://docs.elevenlabs.io/speech-synthesis/models)

---

**replace_strings.txt**

Here you can add strings that will be replaced by other strings in the OCR Text. Sometimes Tesseract will misread l (L) for 1 (one), or 'I for a T, or sometimes you wish that your character name wasn't in the text, because your goal is to generate voices to be used by other players, so making them as generic as possible, and having to remove your character name everytime you want to create a voice file would be very annoying. Well, just add your character name followed by ,"" and it will remove it, here is a example:

yourcharname,""  
'I,I  
something,anotherthing  
.  
.  
.

---

**tesseract_lang.txt**

Here you can add the language Tesseract will analyze in your text, for more information of what languages are support by Tesseract, go to this [link](https://github.com/ils94/LOTROToSpeech/blob/master/Helpful%20Stuffs/Languages/Tesseract%20Supported%20Languages.txt)

By default, Tesseract is set to analyze "eng" (English) text, for others languages, you should mark additional languages to be downloaded and installed during Tesseract installation.

Lord of the Rings Online support 3 languages: English (eng), Deutsch (deu) and Français (fra)

If you play the game in both Deutsch and Français, and are using the LTSET (LOTRO To Speech - Edge-TTS Version), you must do these tweaks for it to be fully functional:

In the root folder of LTSET, you will find a folder called "Resources", and inside that folder there is another folder called "NPCs". By default the npcs.txt is the English version of the npcs names, so if you want to switch to Deutsch (deu), you should rename npcs.txt to npcsEN.txt and rename npcsDE.txt to npcs.txt, that way, LTSET and LTSEL should be able to detect the correct npcs in your set language.

Then, you will have to add the proper voices for female and male in "C:\Users\YOURUSER\Documents\LOTROToSpeech\Voices". There, you will find 2 files named Female Voices.txt and Male Voices.txt. You must save at least one voice model inside each folder that are compatible with your set language, otherwise it will fallback to the default English voice A.I and the result will be weird.

You can see the voice models available for Edge-TTS in these links:

[All Voice Models + information about them](https://github.com/ils94/LOTROToSpeech/blob/master/Helpful%20Stuffs/Languages/List%20of%20voices%20available%20in%20Edge%20TTS.txt)

[Simplified file containing all voices available](https://github.com/ils94/LOTROToSpeech/blob/master/Helpful%20Stuffs/Languages/All%20Voice%20Models%20Female%20and%20Male%20Available%20(Easy%20to%20copy%20paste).txt)

---

**tesseract_path.txt**

Finally, in this file you can add a custom path to your Tesseract installation. By default, Tesseract is installed in either:

- C:\Users\YOURUSER\AppData\Local\Programs\Tesseract-OCR\tesseract.exe
- C:\Program Files\Tesseract-OCR\tesseract.exe

But if you installed Tesseract somewhere else, just open tesseract_path.txt and save the custom path in there.

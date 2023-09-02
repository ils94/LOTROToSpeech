# Modding LOTRO To Speech

You can mod LOTRO To Speech. This is an important part because here you will learn how to put your prefered voice models, and add your own images to detect your Quest Window (very important if you use Interface Addons)

# Adding your voice models

You can add your voice models that are compatible with either Edge-TTS and Elevenlab-TTS

Lets start with LTSET (LOTRO To Speech - Edge-TTS)

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

For the LTSEL (LOTRO To Speech - Elevenlab-TTS) the idea is the same, but of course, you will use voice models compatible with Elevenlabs:

Arnold  
Alex  
John  
.  
.  
.  

As you can see, Elevenlabs use simple names for their voice name models.

# Images used for detecting if Quest Window is open

If you use Interface Addons that change Quest Window appearence, well, LOTRO To Speech may not work, because it's default configuration is to look for vanilla sprites in the Quest Windows.

But don't worry! You can still use your Interface Addon, but you will need to feed LOTRO To Speech the knowledge of what it should look for to detect if the Quest Window is open in your Interface Addon.

For this, all you have to do is to take pictures of parts of your Quest Window. I recommend using Windows Snipping Tool.

With Snipping Tool, you can precisely take some image cues of your Quest Window like some unique button, text label, icon and so on.

After taking the picture, you should save them in:

C:\Users\YOURUSER\Documents\LOTROToSpeech\Detection

The formats supported for the detection images are: PNG, JPG and JPEG.

When LOTRO To Speech detect any of these files extensions in that directory, it will use them to do Pixel Recognition, instead of the default images in the LTS root folder.

# Other configurations

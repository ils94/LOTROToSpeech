# Configuring LOTRO to Speech - Elevenlab TTS Version

Open your game and look for a NPC with a quest available so you can use it as base:

![enter image description here](https://github.com/ils94/LOTROToSpeech/blob/master/Tutorial/Images/tutorial1.PNG?raw=true)

**Tip:** Increase the font size of the quest window, to increase the accurecy of the OCR detection.

Now open LOTRO To Speech overlay and hold Ctrl + Left Mouse Button to drag a rectangle around the text of the quest:

![enter image description here](https://github.com/ils94/LOTROToSpeech/blob/master/Tutorial/Images/tutorial2.PNG?raw=true)

**Tip:** Try to adjust the rectangle edges a bit close to the text, but not so close. That way, the OCR has less area to scan.

While in the LOTRO To Speech overlay, you can use the **OCR Result** window by pressing **Ctrl + A** to quickly preview the OCR Result and see if the text is being captured. The **Menu - Refresh OCR** can be used to quickly refresh the OCR data and show how is the text beind capture in real time.

![enter image description here](https://github.com/ils94/LOTROToSpeech/blob/master/Tutorial/Images/tutorial3.PNG?raw=true)

**Tip:** Resize the Quest Window as much as you can, and leave the it away from your Chat, because if you leave it close, the OCR may read your chat window. Also, increase the font size of the Quest Window, but do not increase it too much, else, the text will become too big and will add Scrollbars. The text must be 100% visible in the screen for the OCR to detect it.

Now, you will need to save your API Key in the api_key.txt file in your: 

C:\Users\YOURUSER\Documents\LOTROToSpeech\Configs\api_key.txt

To find your API Key:

- Go to https://elevenlabs.io/
- Login/create your account
- Click your profile picture
- Click in Profile
- Click the Eye icon to reveal your API Key and copy it
- Open the api_key.txt in the path mentioned above
- paste it in the file and save

This is a very important step if you want to use the Elevenlabs version, because without the API Key, it not possible to use their API to generate the audio files.

After you are done setting everything, you can minimize it (do not close LOTRO To Speech) and press "Ctrl + Alt" to enable the TTS.

Now, you are ready for the next step:

[Modding LOTRO To Speech](https://github.com/ils94/LOTROToSpeech/blob/master/Tutorial/Files/modding.md)

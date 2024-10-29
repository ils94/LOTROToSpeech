from elevenlabs.client import ElevenLabs
import globalVariables


def load_api_key():
    key = ""

    try:
        with open(globalVariables.config_path + r"/api_key.txt", "r") as file:
            lines = file.readlines()

            if len(lines) > 0:
                key = lines[0].strip()

            return key
    except FileNotFoundError:
        return ""


def get_elevenlabs_default_voice():
    client = ElevenLabs(api_key=load_api_key())

    response = client.voices.get_all()

    male_voice = next((voice for voice in response.voices if voice.labels.get("gender") == "male"), None)
    female_voice = next((voice for voice in response.voices if voice.labels.get("gender") == "female"), None)

    selected_voice = male_voice if male_voice else female_voice

    if selected_voice:
        print(f"Using voice: {selected_voice.name}")
        return selected_voice.name
    else:
        print("No male or female voice found.")
        return ""

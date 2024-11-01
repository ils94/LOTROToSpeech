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


def show_all_available_voices():
    client = ElevenLabs(api_key=load_api_key())

    response = client.voices.get_all()

    male_voices = [voice.name for voice in response.voices if voice.labels.get("gender") == "male"]
    female_voices = [voice.name for voice in response.voices if voice.labels.get("gender") == "female"]

    # Build the string output
    result = "Male voices:\n" + "\n".join(male_voices) + "\n\nFemale voices:\n" + "\n".join(female_voices)

    return result

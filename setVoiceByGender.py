import getNPCNameFromPluginOutput
import getVoicesFromFile
import retriveSaveNPCsVoices


def set_voice(engine):
    gender, npc_name = getNPCNameFromPluginOutput.get_npc_gender_by_name()

    if gender:
        if gender == "male":

            if npc_name:

                model = retriveSaveNPCsVoices.get_voice_by_name(npc_name)

            else:

                model = getVoicesFromFile.get_voice("Voice Models/Male Voices.txt")

            if model:

                new_info = {'Name': npc_name, 'Voice': model}

                retriveSaveNPCsVoices.add_info_to_json(new_info)

                return model
            else:
                if engine == "elevenlabs":
                    return "Arnold"

                return "en-US-ChristopherNeural"
        if gender == "female":

            if npc_name:

                model = retriveSaveNPCsVoices.get_voice_by_name(npc_name)

            else:

                model = getVoicesFromFile.get_voice("Voice Models/Female Voices.txt")

            if model:

                new_info = {'Name': npc_name, 'Voice': model}

                retriveSaveNPCsVoices.add_info_to_json(new_info)

                return model
            else:
                if engine == "elevenlabs":
                    return "Bella"

                return "en-GB-SoniaNeural"
        else:
            if engine == "elevenlabs":
                return "Arnold"

            return "en-US-ChristopherNeural"
    else:
        if engine == "elevenlabs":
            return "Arnold"

        return "en-US-ChristopherNeural"

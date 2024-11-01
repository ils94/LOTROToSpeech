import getNPCNameFromPluginOutput
import getVoicesFromFile
import retriveSaveNPCsVoices
import setDefaultVoice
import globalVariables


def set_voice(engine):
    gender, npc_name = getNPCNameFromPluginOutput.get_npc_gender_by_name()

    print(gender, npc_name)

    if gender:
        if gender == "male":

            model = retriveSaveNPCsVoices.get_voice_by_name(npc_name)

            if model:
                return model
            else:
                model = getVoicesFromFile.get_voice("Resources/Voice Models/Male Voices.txt")

                new_info = {'Name': npc_name, 'Voice': model}

                retriveSaveNPCsVoices.add_info_to_json(new_info)

                return model
        if gender == "female":

            model = retriveSaveNPCsVoices.get_voice_by_name(npc_name)

            if model:
                return model
            else:

                model = getVoicesFromFile.get_voice("Resources/Voice Models/Female Voices.txt")

                new_info = {'Name': npc_name, 'Voice': model}

                retriveSaveNPCsVoices.add_info_to_json(new_info)

                return model
        else:
            if engine == "elevenlabs":
                return globalVariables.elevenlabs_default_voice

            return setDefaultVoice.default_voice()
    else:
        if engine == "elevenlabs":
            return globalVariables.elevenlabs_default_voice

        return setDefaultVoice.default_voice()

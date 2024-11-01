from plyer import notification
import globalVariables


def enable_disable_tts():
    if globalVariables.enable_disable:
        globalVariables.enable_disable = False

        notification.notify(
            title="LOTRO To Speech",
            message="TTS is now Disabled",
            app_icon="Resources/lotrotospeech.ico",
            app_name="LOTRO To Speech",
            timeout=3
        )

    else:
        globalVariables.enable_disable = True

        notification.notify(
            title="LOTRO To Speech",
            message="TTS is now Enabled",
            app_icon="Resources/lotrotospeech.ico",
            app_name="LOTRO To Speech",
            timeout=3
        )

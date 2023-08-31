from plyer import notification
import globalVariables


def enable_disable_tts():
    if globalVariables.enable_disable:
        globalVariables.enable_disable = False

        notification.notify(
            title="LOTRO To Speech",
            message="TTS is now Disabled"
            # Specify the duration (in seconds) the notification should be displayed
        )

    else:
        globalVariables.enable_disable = True

        notification.notify(
            title="LOTRO To Speech",
            message="TTS is now Enabled"
            # Specify the duration (in seconds) the notification should be displayed
        )

# this script toggles the system mute state on and off


from pynput.keyboard import Controller, Key

keyboard = Controller()

def run():
    keyboard.press(Key.media_volume_mute)
    keyboard.release(Key.media_volume_mute)


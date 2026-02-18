# this script toggles the system play pause state on and off


from pynput.keyboard import Controller, Key

keyboard = Controller()

def run():
    keyboard.press(Key.media_play_pause)
    keyboard.release(Key.media_play_pause)

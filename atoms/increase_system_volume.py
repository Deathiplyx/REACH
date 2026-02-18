# this script increases the system volume by 10 steps

from pynput.keyboard import Controller, Key
keyboard = Controller()

def run():
    for _ in range(10):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)

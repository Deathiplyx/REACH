# this script is used to open the first result on google after searching for something, by hitting tab, enter, enter

from pynput.keyboard import Controller, Key

keyboard = Controller()

def run():
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
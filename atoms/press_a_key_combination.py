# this code presses a different key combination based on the input recieved from another function
# it should be used for ctrl + k or ctrl + shift + '=' or others ( will add later if I think of more)

from pynput.keyboard import Controller, Key
keyboard = Controller()


def run(firstKey, secondKey, thirdKey=None):
    if thirdKey:
        with keyboard.pressed(firstKey):
            with keyboard.pressed(secondKey):
                keyboard.press(thirdKey)
                keyboard.release(thirdKey)
    else:
        with keyboard.pressed(firstKey):
            keyboard.press(secondKey)
            keyboard.release(secondKey)

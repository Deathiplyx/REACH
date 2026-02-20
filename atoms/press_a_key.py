# this code presses a key combination based on the input recieved from another function


from pynput.keyboard import Controller, Key
keyboard = Controller()



def run(key):
    keyboard.press(key)
    keyboard.release(key)
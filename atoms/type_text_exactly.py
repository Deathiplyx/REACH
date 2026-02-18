# this script is used to recieve input from a separate script and type it out using pynput

from pynput.keyboard import Controller, Key

keyboard = Controller()


def run(text):
    keyboard.type(text)

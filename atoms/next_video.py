# this script is used to enter a key combo to go to the next youtube video, which is shift n

from atoms.press_a_key_combination import run as press_a_key_combination
from pynput.keyboard import Key

def run():
    firstKey = Key.shift
    secondKey = "n"
    press_a_key_combination(firstKey, secondKey)
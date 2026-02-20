# this script is meant to go forward a page on chrome

from atoms.press_a_key_combination import run as press_a_key_combination
from pynput.keyboard import Key

def run():
    firstKey = Key.alt_l
    secondKey = Key.right
    press_a_key_combination(firstKey, secondKey)
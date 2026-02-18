# this script is meant to go back a page on chrome

from press_a_key_combination import run as press_a_key_combination
from pynput.keyboard import Key

def run():
    firstKey = Key.alt_l
    secondKey = Key.left
    press_a_key_combination(firstKey, secondKey)
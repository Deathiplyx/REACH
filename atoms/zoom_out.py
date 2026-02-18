# this function is to zoom out on google chrome, using our premade code in the atoms folder, this is used in the navigate.py file to zoom out when the user says "zoom out"
from pynput.keyboard import Controller, Key
from press_a_key_combination import run as press_a_key_combination

firstKey = Key.ctrl_l
secondKey = "-"

def run():
    press_a_key_combination(firstKey, secondKey)
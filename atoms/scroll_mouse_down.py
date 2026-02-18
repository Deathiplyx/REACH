# this code is used to scroll the mouse down a predetermined amount
from pynput.mouse import Controller, Button
mouse = Controller()
def run():
    for _ in range(8):
        mouse.scroll(0, -1)

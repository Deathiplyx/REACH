from get_the_list_of_open_windows import run as get_windows_info
from press_a_key_combination import run as press_a_key_combination
from pynput.keyboard import Controller, Key
from pywinauto import Desktop
firstKey = Key.ctrl_l
secondKey = "k"

info = get_windows_info()

if not info["chrome_focused"]:
    desktop = Desktop(backend="uia")
    chrome_windows = desktop.windows(title_re=".*Google Chrome$")
    if chrome_windows:
        chrome_windows[0].set_focus()
    press_a_key_combination(firstKey, secondKey)
else:
    print("Is focused.")
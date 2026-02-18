# this script is used to check chrome windows state (whether it exists or not)
# it also checks if the web browser is focused or not, and returns the active tab name as well
# this is used to determine if the user is currently looking at a specific tab or not, and to get the name of that tab for context
# this script was coded with the help of pywinauto documentation and some trial and error, as well as some help from chatgpt to figure out how to get the active tab name and check if the window is focused or not

from pywinauto import Desktop
import time


def clean_title(title):
    # Remove Chrome window suffix
    if title.endswith(" - Google Chrome"):
        title = title.replace(" - Google Chrome", "")
    
    # Remove memory usage suffix if present
    if " - Memory usage" in title:
        title = title.split(" - Memory usage")[0]
    
    return title.strip()


def run():
    time.sleep(1)

    desktop = Desktop(backend="uia")

    # Find Chrome window
    chrome_windows = desktop.windows(title_re=".*Google Chrome$")

    if not chrome_windows:
        return "fail"

    chrome_window = chrome_windows[0]

    # Active tab = window title (most reliable method)
    active_tab = clean_title(chrome_window.window_text())

    # Get all UIA TabItem controls
    tab_items = chrome_window.descendants(control_type="TabItem")

    # Extract text
    raw_titles = [tab.window_text() for tab in tab_items]

    # Filter out non-browser tabs
    # Real Chrome tabs usually contain " - "
    tab_titles = []
    for title in raw_titles:
        if title and " - " in title:
            tab_titles.append(clean_title(title))

    # Check if Chrome window itself is focused
    try:
        chrome_focused = chrome_window.has_keyboard_focus()
    except:
        chrome_focused = False

    return {
        "tab_titles": tab_titles,
        "active_tab": active_tab,
        "chrome_focused": chrome_focused
    }
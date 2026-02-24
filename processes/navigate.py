#this program is used to navigate google chrome using the code in the atoms folder, to do stuff like scrolling up and down, and to zoom in and out, or going forward and back a page
#and to open the first result on google after searching for something or to go to the next youtube video
# or to type something or type it and enter it, or to just enter, this is if you want to continue a convo with a friend or AI etc.


#programs used in navigate


#atoms -

#zoom_out

#zoom_in

#wait_for_a_number_of_seconds

#scroll_mouse_up


#scroll_mouse_down


#open_first_result


#next_video


#go_forward


#go_back


#press_a_key - this should be used to hit enter when typing some text and entering it


#type_text_exactly - this should be used if someone just wants to type something

#we should have type, and type and enter, and just enter as navigate things

# processes/navigate.py
# Handles the "navigate" wake word.
# Controls browser navigation, scrolling, zoom, and simple typing.

from atoms.zoom_in import run as zoom_in
from atoms.zoom_out import run as zoom_out
from atoms.scroll_mouse_up import run as scroll_up
from atoms.scroll_mouse_down import run as scroll_down
from atoms.go_back import run as go_back
from atoms.go_forward import run as go_forward
from atoms.open_first_result import run as open_first_result
from atoms.next_video import run as next_video
from atoms.press_a_key import run as press_key
from atoms.type_text_exactly import run as type_text
from atoms.wait_for_a_number_of_seconds import run as wait
from pynput.keyboard import Key, Controller
from reach_language import NAVIGATE_COMMANDS


def contains_phrase(text, phrases):
    for phrase in phrases:
        if phrase in text:
            return True
    return False


def run(text):
    if not text:
        return "fail"

    command = text.lower().strip()

    # --- Zoom ---
    if contains_phrase(command, NAVIGATE_COMMANDS["zoom_in"]):
        zoom_in()
        return "success"

    if contains_phrase(command, NAVIGATE_COMMANDS["zoom_out"]):
        zoom_out()
        return "success"

    # --- Scroll ---
    if contains_phrase(command, NAVIGATE_COMMANDS["scroll_up"]):
        scroll_up()
        return "success"

    if contains_phrase(command, NAVIGATE_COMMANDS["scroll_down"]):
        scroll_down()
        return "success"

    # --- History ---
    if contains_phrase(command, NAVIGATE_COMMANDS["back"]):
        go_back()
        return "success"

    if contains_phrase(command, NAVIGATE_COMMANDS["forward"]):
        go_forward()
        return "success"

    # --- Results / media ---
    if contains_phrase(command, NAVIGATE_COMMANDS["open_first"]):
        open_first_result()
        return "success"
        # --- TAB ---
    if contains_phrase(command, NAVIGATE_COMMANDS["tab"]):
        press_key(Key.tab)
        wait(0.2)
        return "success"
    # --- Typing ---
    if command.startswith("type "):
        content = command[len("type "):]

        if content.endswith(" and enter"):
            content = content[:-10]
            type_text(content)
            wait(0.1)
            press_key(Key.enter)
            return "success"

        type_text(content)
        return "success"

    # --- Enter only ---
    if contains_phrase(command, NAVIGATE_COMMANDS["enter"]):
        press_key(Key.enter)
        return "success"

    return "fail"
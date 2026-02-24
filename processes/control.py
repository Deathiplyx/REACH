# this script is used to do common media controls like pause and unpause and mute and volume up and down, using our premade code in the atoms folder


#programs used in control -

#atoms -


#decrease_system_volume

#increase_system_volume

#next_video - i figure this can be in both control and navigate

#wait_for_a_number_of_seconds

#toggle_system_mute

#send_play_pause_media_command

# processes/control.py
# Handles media/system control commands using flexible language matching

from atoms.decrease_system_volume import run as decrease_volume
from atoms.increase_system_volume import run as increase_volume
from atoms.toggle_system_mute import run as toggle_mute
from atoms.send_play_pause_media_command import run as play_pause
from atoms.next_video import run as next_video
from atoms.wait_for_a_number_of_seconds import run as wait
from atoms.press_a_key import run as press_key
from pynput.keyboard import Key, Controller
from reach_language import CONTROL_COMMANDS


def contains_phrase(text, phrases):
    for phrase in phrases:
        if phrase in text:
            return True
    return False


def run(text):
    if not text:
        return "fail"

    command = text.lower().strip()


    # --- TAB ---
    if contains_phrase(command, CONTROL_COMMANDS["tab"]):
        press_key(Key.tab)
        wait(0.2)
        return "success"

    # --- PLAY / PAUSE ---
    if contains_phrase(command, CONTROL_COMMANDS["play_pause"]):
        play_pause()
        return "success"

    # --- MUTE ---
    if contains_phrase(command, CONTROL_COMMANDS["mute"]):
        toggle_mute()
        return "success"

    # --- VOLUME UP ---
    if contains_phrase(command, CONTROL_COMMANDS["volume_up"]):
        increase_volume()
        wait(0.2)
        return "success"

    # --- VOLUME DOWN ---
    if contains_phrase(command, CONTROL_COMMANDS["volume_down"]):
        decrease_volume()
        wait(0.2)
        return "success"

    # --- NEXT TRACK / VIDEO ---
    if contains_phrase(command, CONTROL_COMMANDS["next"]):
        next_video()
        return "success"

    return "fail"
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
# This process handles the "control" wake word.
# It performs common media controls using atomic scripts.

from atoms.decrease_system_volume import run as decrease_volume
from atoms.increase_system_volume import run as increase_volume
from atoms.toggle_system_mute import run as toggle_mute
from atoms.send_play_pause_media_command import run as play_pause
from atoms.next_video import run as next_video
from atoms.wait_for_a_number_of_seconds import run as wait


def run(text):
    if not text:
        return "fail"

    command = text.lower().strip()

    # --- REMOVE WAKE WORD IF PRESENT ---
    if command.startswith("control "):
        command = command[len("control "):]
    elif command == "control":
        return "fail"

    # --- Play / Pause ---
    if "pause" in command or "play" in command:
        play_pause()
        return "success"

    # --- Mute ---
    if "mute" in command:
        toggle_mute()
        return "success"

    # --- Volume Up ---
    if "volume up" in command or "louder" in command:
        increase_volume()
        wait(0.2)
        return "success"

    # --- Volume Down ---
    if "volume down" in command or "quieter" in command:
        decrease_volume()
        wait(0.2)
        return "success"

    # --- Next Video / Track ---
    if "next" in command or "skip" in command:
        next_video()
        return "success"

    return "fail"
# this code waits for the user to press a button for push to talk
# first press = start recording
# second press = stop recording and send audio

from pynput import keyboard
from return_the_recorded_audio import start as start_recording
from return_the_recorded_audio import stop as stop_recording

# The key combination to check
COMBINATION = {keyboard.Key.shift_l, keyboard.Key.ctrl_l}

# Currently active keys
current = set()

# Toggle state
state = False

# Listener reference
listener = None


def on_press(key):
    global state, listener

    if key in COMBINATION:
        current.add(key)

        if all(k in current for k in COMBINATION):
            state = not state

            if state:
                print("Button pressed, starting voice input...")
                start_recording()
            else:
                print("Ended voice input.")
                audio_file = stop_recording()
                if audio_file:
                    print(f"Send to STT: {audio_file}")

                # STOP LISTENER AFTER SESSION
                listener.stop()


def on_release(key):
    if key in current:
        current.remove(key)


def run():
    global listener
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    listener.join()
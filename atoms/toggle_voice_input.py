# this code waits for the user to press a button for push to talk
# first press = start recording
# second press = stop recording and return audio file

from pynput import keyboard
from atoms.return_the_recorded_audio import start as start_recording
from atoms.return_the_recorded_audio import stop as stop_recording

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

    # Prevent repeat triggers while keys are held
    if getattr(on_press, "triggered", False):
        return

    if key in COMBINATION:
        current.add(key)

        if all(k in current for k in COMBINATION):
            on_press.triggered = True
            state = not state

            if state:
                print("Button pressed, starting voice input...")
                start_recording()
            else:
                print("Ended voice input.")
                audio_file = stop_recording()

                if audio_file:
                    print(f"Send to STT: {audio_file}")
                    listener.audio_file = audio_file

                # Stop listener after one full session
                listener.stop()


def on_release(key):
    if key in current:
        current.remove(key)

    # Allow next trigger after keys released
    on_press.triggered = False


def run():
    global listener, state, current

    # Reset session state every time run() is called
    state = False
    current = set()
    on_press.triggered = False

    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    listener.join()

    return getattr(listener, "audio_file", None)

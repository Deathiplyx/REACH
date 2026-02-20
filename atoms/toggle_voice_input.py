# this code waits for the user to press a button for push to talk
# first press = start recording
# second press = stop recording and return audio file
# ALSO supports manual start/stop for frontend use

from pynput import keyboard
from atoms.return_the_recorded_audio import start as start_recording
from atoms.return_the_recorded_audio import stop as stop_recording
import os
import time

BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # REACH root
AUDIO_PATH = os.path.join(BASE_DIR, "audio", "network_audio.webm")

# The key combination to check
COMBINATION = {keyboard.Key.shift_l, keyboard.Key.ctrl_l}

# Currently active keys
current = set()

# Toggle state
state = False

# Listener reference
listener = None

# For manual (frontend) mode
manual_audio_file = None


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


# -------- Manual control (for frontend / future glasses) --------

def start_manual():
    global state
    if not state:
        state = True
        print("Manual start recording...")
        start_recording()


def stop_manual():
    global state, manual_audio_file
    if state:
        state = False
        print("Manual stop recording...")
        manual_audio_file = stop_recording()
        return manual_audio_file
    return None


# -------- Main entry --------

def run(mode="keyboard"):
    global listener, state, current, manual_audio_file

    # Reset session state every time run() is called
    state = False
    current = set()
    manual_audio_file = None
    on_press.triggered = False

    # --- Keyboard mode ---
    if mode == "keyboard":
        listener = keyboard.Listener(on_press=on_press, on_release=on_release)
        listener.start()
        listener.join()
        return getattr(listener, "audio_file", None)

    # --- Manual mode (network audio polling) ---
    elif mode == "manual":
        print("========== MANUAL AUDIO MODE ==========")
        print("Looking for file at:")
        print(AUDIO_PATH)
        print("Absolute path exists:", os.path.exists(AUDIO_PATH))
        print("========================================")

        last_modified = None

        if os.path.exists(AUDIO_PATH):
            last_modified = os.path.getmtime(AUDIO_PATH)
            print("Initial file timestamp:", last_modified)
        else:
            print("File does NOT exist yet. Waiting for upload...")

        while True:
            # Debug heartbeat so you know loop is alive
            print("[DEBUG] Checking for audio file...")
        
            if os.path.exists(AUDIO_PATH):
                try:
                    current_modified = os.path.getmtime(AUDIO_PATH)
                    file_size = os.path.getsize(AUDIO_PATH)

                    print(f"[DEBUG] File found | size={file_size} bytes | modified={current_modified}")

                    # Ignore empty files (upload not finished)
                    if file_size == 0:
                        print("[DEBUG] File size is 0 — waiting for upload to finish...")
                        time.sleep(0.5)
                        continue

                    # Detect new upload
                    if last_modified is None or current_modified != last_modified:
                        print("[DEBUG] New or updated audio detected!")
                        last_modified = current_modified

                        # Extra wait to ensure write is complete
                        time.sleep(1)

                        print(">>> AUDIO READY FOR STT <<<")
                        return AUDIO_PATH

                except Exception as e:
                    print("[ERROR] Problem reading file:", e)

            else:
                print("[DEBUG] File not found yet.")

            time.sleep(0.5)
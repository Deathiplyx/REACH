import os
import time

# Get REACH root (this file is in atoms/)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Match what the server actually saves
AUDIO_PATH = os.path.join(BASE_DIR, "audio", "network_audio.webm")


def run():
    print("Waiting for network audio...")
    print("[DEBUG] Looking at:", AUDIO_PATH)

    while True:
        if os.path.exists(AUDIO_PATH):
            size = os.path.getsize(AUDIO_PATH)
            print(f"[DEBUG] Found file, size={size}")

            if size > 0:
                print("Audio file detected.")
                return AUDIO_PATH

        time.sleep(0.5)
# this script provides start and stop functions for audio recording
# toggle_voice_input should call start() and stop()

import os
import sounddevice as sd
import numpy as np
import soundfile as sf

samplerate = 16000
recording_buffer = []
is_recording = False
stream = None


def _callback(indata, *args):
    global recording_buffer
    if is_recording:
        recording_buffer.append(indata.copy())


def start():
    global stream, is_recording, recording_buffer

    if is_recording:
        return

    print("Recording started...")
    recording_buffer = []
    is_recording = True

    stream = sd.InputStream(
        samplerate=samplerate,
        channels=1,
        callback=_callback
    )
    stream.start()


def stop():
    global stream, is_recording

    if not is_recording:
        return None

    print("Recording stopped.")
    is_recording = False

    stream.stop()
    stream.close()

    if not recording_buffer:
        return None

    audio_array = np.concatenate(recording_buffer, axis=0)
    base_dir = os.path.dirname(os.path.dirname(__file__))
    filename = os.path.join(base_dir, "audio", "recorded_audio.wav")

    sf.write(filename, audio_array, samplerate)

    print(f"Audio saved to {filename}")

    return filename
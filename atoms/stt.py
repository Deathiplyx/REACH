# this script is for speech to text conversion
# it now uses the audio file that is passed in (network or local)

from faster_whisper import WhisperModel
import math
import os

model = WhisperModel("base")


def run(audio_file):
    # --- Make path absolute if needed ---
    if not os.path.isabs(audio_file):
        base_dir = os.path.dirname(os.path.dirname(__file__))  # REACH root
        audio_file = os.path.join(base_dir, audio_file)

    # --- Debug ---
    print("[STT] Loading audio from:", audio_file)

    if not os.path.exists(audio_file):
        print("[STT ERROR] File does not exist.")
        return {
            "text": "",
            "confidence": 0.0
        }

    # --- Transcribe ---
    segments, info = model.transcribe(audio_file)

    text_parts = []
    logprobs = []

    for segment in segments:
        text_parts.append(segment.text)
        logprobs.append(segment.avg_logprob)

    text = "".join(text_parts).strip()

    # --- Confidence estimate ---
    if logprobs:
        avg_logprob = sum(logprobs) / len(logprobs)
        confidence = math.exp(avg_logprob)
    else:
        confidence = 0.0

    return {
        "text": text,
        "confidence": confidence
    }
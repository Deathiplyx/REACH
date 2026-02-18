# this script is for speech to text conversion, chat gpt helped format this
# it loads the audio from REACH/audio/recorded_audio.wav

from faster_whisper import WhisperModel
import math
import os

model = WhisperModel("base")


def run():
    # Get path to REACH root
    base_dir = os.path.dirname(os.path.dirname(__file__))

    # Path to audio file
    audio_file = os.path.join(base_dir, "audio", "recorded_audio.wav")

    segments, info = model.transcribe(audio_file)

    text_parts = []
    logprobs = []

    for segment in segments:
        text_parts.append(segment.text)
        logprobs.append(segment.avg_logprob)

    text = "".join(text_parts).strip()

    # Average log probability
    if logprobs:
        avg_logprob = sum(logprobs) / len(logprobs)
        confidence = math.exp(avg_logprob)
    else:
        confidence = 0.0

    return {
        "text": text,
        "confidence": confidence
    }

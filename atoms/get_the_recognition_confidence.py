# this script runs the STT and splits the result into text and confidence

from stt import run as stt_run


def run():
    # Call STT (no arguments)
    stt_output = stt_run()

    # Extract values safely
    text = stt_output.get("text", "")
    confidence = stt_output.get("confidence", 0.0)

    return text, confidence



text, confidence = run()
print(text)
print(confidence)
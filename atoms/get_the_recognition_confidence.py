# this script runs the STT and splits the result into text and confidence


def run(stt_output):

    # Extract values safely
    text = stt_output.get("text", "")
    confidence = stt_output.get("confidence", 0.0)

    return text, confidence
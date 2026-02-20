# main_stt.py
# REACH - Unified Voice Input Pipeline
# Handles: network audio -> STT -> confidence -> wake word

from atoms.stt import run as stt_run
from atoms.get_the_recognition_confidence import run as get_confidence
from atoms.get_the_recognized_text_and_find_wake_word_and_trim_it_and_store_wake_word_as_wake_word import run as parse_wake_word
from atoms.speak_text_to_the_user import run as speak
from atoms.wait_for_a_number_of_seconds import run as wait
from atoms.wait_for_network_audio import run as wait_for_network_audio

import os


CONFIDENCE_THRESHOLD = 0.35


def run():
    # 1. Wait for audio from server/frontend
    print("Waiting for voice input...")
    audio_file = wait_for_network_audio()

    # Debug: confirm what we received
    print("[DEBUG] Audio path returned:", audio_file)

    if not audio_file:
        print("[DEBUG] No audio file returned")
        speak("I did not hear anything.")
        return "fail", ""

    if not os.path.exists(audio_file):
        print("[DEBUG] File does not exist:", audio_file)
        speak("Audio file not found.")
        return "fail", ""

    print("[DEBUG] File exists. Size:", os.path.getsize(audio_file), "bytes")

    # 2. Run STT
    print("[DEBUG] Running STT...")
    stt_output = stt_run(audio_file)

    # Remove file so it won't be reused
    try:
        os.remove(audio_file)
        print("[DEBUG] Audio file removed after processing")
    except Exception as e:
        print("[DEBUG] Could not remove file:", e)

    # 3. Extract text + confidence
    text, confidence = get_confidence(stt_output)

    print("[DEBUG] Confidence:", confidence)
    print("[DEBUG] Text:", text)

    if confidence < CONFIDENCE_THRESHOLD:
        print("Low confidence:", confidence)
        speak("Please repeat that.")
        return "fail", ""

    if not text:
        speak("I did not understand.")
        return "fail", ""

    # 4. Parse wake word
    wake_word, content = parse_wake_word(text)

    print("[DEBUG] Wake word:", wake_word)
    print("[DEBUG] Content:", content)

    if wake_word == "fail":
        speak("Please start your command with a valid wake word.")
        return "fail", ""

    # 5. Small delay (stability)
    wait(0.2)

    # 6. Return to main
    return wake_word, content
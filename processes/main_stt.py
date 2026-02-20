# main_stt.py
# REACH - Unified Voice Input Pipeline
# Handles: toggle -> record -> STT -> confidence -> wake word -> output


from atoms.toggle_voice_input import run as toggle_voice_input
from atoms.return_the_recorded_audio import start as start_recording
from atoms.return_the_recorded_audio import stop as stop_recording
from atoms.stt import run as stt_run
from atoms.get_the_recognition_confidence import run as get_confidence
from atoms.get_the_recognized_text_and_find_wake_word_and_trim_it_and_store_wake_word_as_wake_word import run as parse_wake_word
from atoms.speak_text_to_the_user import run as speak
from atoms.wait_for_a_number_of_seconds import run as wait


CONFIDENCE_THRESHOLD = 0.35


def run():
    # 1. Wait for user push-to-talk
    print("Waiting for voice input...")
    audio_file = toggle_voice_input()


    if not audio_file:
        speak("I did not hear anything.")
        return "fail", ""

    # 3. Run STT
    stt_output = stt_run(audio_file)

    # 4. Extract confidence
    text, confidence = get_confidence(stt_output)

    if confidence < CONFIDENCE_THRESHOLD:
        print("Low confidence:", confidence)
        speak("Please repeat that.")
        return "fail", ""

    # 5. Extract text
    print("Recognized:", text)

    if not text:
        speak("I did not understand.")
        return "fail", ""

    # 6. Parse wake word
    wake_word, content = parse_wake_word(text)

    if wake_word == "fail":
        speak("Please start your command with a valid wake word.")
        return "fail", ""

    # 7. Small stabilization delay
    wait(0.2)

    # 8. Return structured result to main
    return wake_word, content
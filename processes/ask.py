# processes/ask.py
# This process handles the "ask" wake word.
# It opens ChatGPT, types the question, and submits it.

from atoms.open_browser import run as open_browser
from atoms.press_a_key import run as press_a_key
from atoms.press_a_key_combination import run as press_a_key_combination
from atoms.type_text_exactly import run as type_text_exactly
from atoms.wait_for_a_number_of_seconds import run as wait_for_a_number_of_seconds

from pynput.keyboard import Key
from reach_language import ASK_PREFIXES


def clean_ask_text(text):
    """
    Removes common ask prefixes so the question
    sent to ChatGPT is clean.
    """
    command = text.lower().strip()

    for prefix in ASK_PREFIXES:
        if command.startswith(prefix + " "):
            return command[len(prefix) + 1:]

    return command


def run(text):
    if not text:
        return "fail"

    # --- Normalize language ---
    question = clean_ask_text(text)

    if not question:
        return "fail"

    # 1. Open browser
    if not open_browser():
        return "fail"

    wait_for_a_number_of_seconds(2)

    # 2. Focus address bar
    press_a_key_combination(Key.ctrl_l, 'l')
    wait_for_a_number_of_seconds(0.5)

    # 3. Go to ChatGPT
    type_text_exactly("https://chatgpt.com")
    press_a_key(Key.enter)

    # 4. Wait for page load
    wait_for_a_number_of_seconds(5)

    # 5. Type question
    type_text_exactly(question)

    # 6. Submit
    press_a_key(Key.enter)

    return "success"
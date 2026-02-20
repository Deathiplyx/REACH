# processes/ask.py
# This process handles the "ask" wake word.
# It opens ChatGPT, types the question, and submits it.

from atoms.open_browser import run as open_browser
from atoms.press_a_key import run as press_a_key
from atoms.press_a_key_combination import run as press_a_key_combination
from atoms.type_text_exactly import run as type_text_exactly
from atoms.wait_for_a_number_of_seconds import run as wait_for_a_number_of_seconds

from pynput.keyboard import Key


def run(text):
    # text example: "what is entropy"
    # or: "explain black holes"

    if not text:
        return "fail"

    # 1. Open browser (opens default browser)
    if not open_browser():
        return "fail"

    # 2. Wait for browser to be ready
    wait_for_a_number_of_seconds(2)

    # 3. Open ChatGPT using address bar
    # Ctrl + L focuses address bar
    press_a_key_combination(Key.ctrl_l, 'l')

    wait_for_a_number_of_seconds(0.5)

    # 4. Type ChatGPT URL
    type_text_exactly("https://chatgpt.com")

    # 5. Go to site
    press_a_key(Key.enter)

    # 6. Wait for ChatGPT to load
    wait_for_a_number_of_seconds(5)

    # 7. Type the user's question
    type_text_exactly(text)

    # 8. Submit the prompt
    press_a_key(Key.enter)

    return "success"
# this code is used to get the recognized text from our stt

# this must also trim the wake word from the beginning of the text but also store the wake word if it exists, and if it doesnt exist return fail


# list of wake words - ask, search, navigate, communicate, control

# this also must store the wake word for later use


def run(text):
    wake_words = ["ask", "search", "navigate", "communicate", "control"]

    text = text.lower().strip()

    for wake_word in wake_words:
        if text.startswith(wake_word):
            # trim the wake word from the beginning of the text
            trimmed_text = text[len(wake_word):].strip()
            return wake_word, trimmed_text

    return "fail", None
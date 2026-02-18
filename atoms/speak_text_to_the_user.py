# this script is used to speak any text through tts that would normally be in console

import pyttsx3

def run(text):
    if text == "":
            engine = pyttsx3.init()
            engine.say("Nothing to speak")
            engine.runAndWait()
    else:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
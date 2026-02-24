# REACH
# Remote Execution And Command Handler

# REACH is a hands-free control system that allows a user to operate their personal computer using voice commands.

# The system listens for user input, interprets intent, and executes actions such as:
# - Performing web searches
# - Controlling media
# - Navigating content
# - Sending messages
# - Interacting with AI tools

# REACH is designed around a simple idea:

# Intent instead of touch.

# The long-term goal is to enable seamless hands-free computing through lightweight interfaces such as phones or smart glasses
# while keeping all processing on the user’s personal machine.


# this will mainly interact with the functions / scripts in the processes folder, which are the 6 main methods of interfacing with the system ( these are written with separate child functions as well)

#processes list - ask, communicate, control, navigate, search


#programs used in main - 


#processes -

#ask


#communicate


#control


#navigate


#search


#atoms - 

#create_a_failure_result

#create_a_success_result



# main.py
# REACH - Remote Execution And Command Handler
# Main control loop


from processes.main_stt import run as get_voice_command

from processes.ask import run as ask
from processes.communicate import run as communicate
from processes.control import run as control
from processes.navigate import run as navigate
from processes.search import run as search

from atoms.create_a_failure_result import run as failure
from atoms.create_a_success_result import run as success
from atoms.speak_text_to_the_user import run as speak

# Language layer
from reach_language import get_wake_word


# Minimum words required per intent
MIN_WORDS_BY_INTENT = {
    "ask": 1,
    "search": 1,
    "navigate": 1,
    "control": 1,
    "communicate": 2   # needs target + message
}


def route_command(wake_word, content):
    if wake_word == "ask":
        return ask(content)

    elif wake_word == "communicate":
        return communicate(content)

    elif wake_word == "control":
        return control(content)

    elif wake_word == "navigate":
        return navigate(content)

    elif wake_word == "search":
        return search(content)

    else:
        return "fail"


def run():
    while True:
        # 1. Get RAW text from STT
        text = get_voice_command()

        if not text or text == "fail":
            print("[MAIN] No valid speech detected")
            failure("fail")
            continue

        text = text.strip()
        print("[MAIN] Raw text:", text)

        # 2. Language layer → intent + content
        wake_word, content = get_wake_word(text)

        print("[MAIN] Intent:", wake_word)
        print("[MAIN] Content:", content)

        # 3. Intent check
        if wake_word == "fail":
            print("[MAIN] No intent detected")
            speak("I didn't understand the command.")
            failure("fail")
            continue

        # 4. Intent-specific content validation
        min_words = MIN_WORDS_BY_INTENT.get(wake_word, 1)

        if not content or len(content.split()) < min_words:
            print(f"[MAIN] Content too short for intent: {wake_word}")

            # Clarification instead of silent failure
            if wake_word == "communicate":
                speak("Who do you want to message and what should I say?")
            elif wake_word == "search":
                speak("What should I search for?")
            elif wake_word == "ask":
                speak("What would you like to ask?")
            elif wake_word == "navigate":
                speak("What should I navigate?")
            elif wake_word == "control":
                speak("What would you like to control?")
            else:
                speak("Please provide more details.")

            failure("fail")
            continue

        # 5. Route to process
        result = route_command(wake_word, content)

        # 6. Result handling
        if result == "success":
            success("success")
        else:
            print("[MAIN] Process returned fail")
            speak("That command didn't work.")
            failure("fail")


# Start REACH
run()
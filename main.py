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
        # 1. Get voice input
        wake_word, content = get_voice_command()

        if wake_word == "fail":
            failure("fail")
            continue

        # 2. Route to correct process
        result = route_command(wake_word, content)

        # 3. Handle result
        if result == "success":
            success("success")
        else:
            failure("fail")


# Start REACH
run()




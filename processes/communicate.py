#this script is used to open discord.com/app and use ctrl k to navigate to the channel or user etc.
#  that the user wants to navigate to, and send a singular message, using our premade code in the atoms folder

# this would be done with ctrl k, and then type in user, hit enter,
#  and hit tab, then type in the message, and then hit enter again to send the message
# 
# this is all done with our premade code in the atoms folder 

# programs used in communicate - 

#atoms -

#get_user_to_communicate_with

#message - this is just getting what the message is

#wait_for_a_number_of_seconds

#type_text_exactly



#also this should just resuse logic from ask, but just change it to open discord.com/app and then hit ctrl k, type users name, wait, hit enter, hit tab, type message, hit enter


# processes/communicate.py
# This process handles the "communicate" wake word.
# It opens Discord Web, finds a user/channel with Ctrl+K,
# then sends a single message.

from atoms.open_browser import run as open_browser
from atoms.press_a_key import run as press_a_key
from atoms.press_a_key_combination import run as press_a_key_combination
from atoms.type_text_exactly import run as type_text_exactly
from atoms.wait_for_a_number_of_seconds import run as wait_for_a_number_of_seconds

from pynput.keyboard import Key


def run(text):
    # Expected example:
    # "john hello how are you"
    # first word = user/channel
    # rest = message

    if not text:
        return "fail"

    # --- Split input ---
    parts = text.split(" ", 1)

    if len(parts) < 2:
        return "fail"

    target = parts[0]
    message = parts[1]

    # 1. Open browser
    if not open_browser():
        return "fail"

    # 2. Wait for browser
    wait_for_a_number_of_seconds(2)

    # 3. Go to Discord
    press_a_key_combination(Key.ctrl_l, 'l')
    wait_for_a_number_of_seconds(0.5)

    type_text_exactly("https://discord.com/app")
    press_a_key(Key.enter)

    # 4. Wait for Discord to load
    wait_for_a_number_of_seconds(6)

    # 5. Open Quick Switcher (Ctrl+K)
    press_a_key_combination(Key.ctrl_l, 'k')
    wait_for_a_number_of_seconds(0.5)

    # 6. Type user/channel name
    type_text_exactly(target)
    wait_for_a_number_of_seconds(1)

    # 7. Select it
    press_a_key(Key.enter)
    wait_for_a_number_of_seconds(1)

    # 8. Move to message box
    press_a_key(Key.tab)
    wait_for_a_number_of_seconds(0.3)

    # 9. Type message
    type_text_exactly(message)

    # 10. Send
    press_a_key(Key.enter)

    return "success"
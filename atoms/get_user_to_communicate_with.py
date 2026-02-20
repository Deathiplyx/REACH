# the job of this script is to determine who the user wants to communicate with, this is used in the communicate.py file to determine who the user wants to send a message to on discord
# then it uses that information to navigate to that user and send the message
# ex use. "with john, how are you? - this would return john as it is the first word after with - the reason communicate is not used in the example
# is because communicate is used as the wake word and is not included
# this should also be able to handle a user with a spaced name so it should cut everything after the keyword message and the word message itself


text = "with john message how are you?"

def run(text):
    text = text.lower().strip()
    if text.startswith("with "):
        # Extract the part after "with "
        remaining_text = text[5:].strip()  # Remove "with " and trim whitespace

        # The recipient is the first word in the remaining text
        recipient = remaining_text.split()[0] if remaining_text else None

        return recipient
    else:
        return "fail"
print(run(text))
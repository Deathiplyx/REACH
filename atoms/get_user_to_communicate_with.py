# the job of this script is to determine who the user wants to communicate with, this is used in the communicate.py file to determine who the user wants to send a message to on discord
# then it uses that information to navigate to that user and send the message
# ex use. "with john, how are you? - this would return john as it is the first word after with - the reason communicate is not used in the example
# is because communicate is used as the wake word and is not included

def run(text):
    if 'with' in text:
        user_to_communicate_with = text.split('with', 1)[1].split(',')[0].strip()
        return user_to_communicate_with
    else:
        return 'fail'
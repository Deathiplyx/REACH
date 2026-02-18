# this script is used to get the mssage the user wants to send to another user on discord

# ex use. "with john, how are you? - this would return how are you? as it is the text after the user - the reason communicate is not used in the example
# is because communicate is used as the wake word and is not included

def run(text):
    if 'with' in text:
        message = text.split('with', 1)[1].split(',', 1)[1].strip()
        return message
    else:
        return 'fail'
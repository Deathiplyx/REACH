# this script is used to get the first word from the stt result, which is used to determine the command to execute

def run(text):
    words = text.split()
    if len(words) > 0:
        return words[0].lower()
    else:
        return 'fail'

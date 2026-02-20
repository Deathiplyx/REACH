# this code should take text and get what a user wants ot search fot from it
# ex. youtube for how to make a cake - should result in - how to make a cake ( the reason the word search isn't in front of youtube is because it is trimmed by another script before hand)

# so this should always just trim anything at or before the word for

def run(text):
    if 'for' in text:
        return text.split('for', 1)[1].strip()
    else:
        return 'fail'
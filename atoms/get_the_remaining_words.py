# this script is used to get any words that aren't specifically a direction in the code, this would include the thing in parentheses in this example ex. youtube for (funny cat videos)
#  the reason search isn't there in the example, is because search is used as the wake word and is not included
# so basically just trim anything before the first use of for in the given text

def run(text):
    if 'for' in text:
        remaining_words = text.split('for', 1)[1].strip()
        return remaining_words
    else:
        return 'fail'
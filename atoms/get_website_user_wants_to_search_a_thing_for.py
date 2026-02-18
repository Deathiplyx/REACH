# this script is used to get the website name that the user is trying to use search parameters on ex. youtube for funny cat videos, this would return youtube

def run(text):
    if 'for' in text:
        website_name = text.split('for', 1)[0].strip()
        return website_name
    else:
        return 'fail'
    
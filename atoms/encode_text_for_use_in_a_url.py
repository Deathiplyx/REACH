# this script is used to make sure text is url friendly, this is used to format the search query for the search script
import urllib.parse

def run(text):
    url_friendly_text = urllib.parse.quote(text)
    return url_friendly_text
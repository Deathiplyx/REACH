# processes/search.py
# This process handles the "search" wake word.

from atoms.get_search import run as get_search
from atoms.get_website_name_as_parameter import run as get_website_name_as_parameter
from atoms.open_browser import run as open_browser
from atoms.press_a_key import run as press_a_key
from atoms.type_text_exactly import run as type_text_exactly
from atoms.wait_for_a_number_of_seconds import run as wait_for_a_number_of_seconds

from pynput.keyboard import Key
from reach_language import SEARCH_SYNONYMS


def clean_search_text(text):
    command = text.lower().strip()

    for prefix in SEARCH_SYNONYMS:
        if command.startswith(prefix + " "):
            return command[len(prefix) + 1:]

    return command


def run(text):
    if not text:
        return "fail"

    # Normalize language
    cleaned_text = clean_search_text(text)

    # Extract search query
    search_query = get_search(cleaned_text)

    if not search_query or search_query == "fail":
        search_query = cleaned_text

    # Site-specific?
    site_parameter = get_website_name_as_parameter(text)

    if site_parameter != "fail":
        final_query = f"{site_parameter} {search_query}"
    else:
        final_query = search_query

    # Open browser
    if not open_browser():
        return "fail"

    wait_for_a_number_of_seconds(2)

    type_text_exactly(final_query)
    press_a_key(Key.enter)

    return "success"
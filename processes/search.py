# processes/search.py
# This process handles the "search" wake word.

from atoms.get_search import run as get_search
from atoms.get_website_name_as_parameter import run as get_website_name_as_parameter
from atoms.open_browser import run as open_browser
from atoms.press_a_key import run as press_a_key
from atoms.type_text_exactly import run as type_text_exactly
from atoms.wait_for_a_number_of_seconds import run as wait_for_a_number_of_seconds

from pynput.keyboard import Key


def run(text):
    # text example: "youtube for funny cats"
    # or: "funny cats"

    # 1. Extract the actual search query
    search_query = get_search(text)

    if not search_query:
        return "fail"

    # 2. Check if this is a site-specific search
    site_parameter = get_website_name_as_parameter(text)

    # 3. Build final query
    if site_parameter != "fail":
        final_query = f"{site_parameter} {search_query}"
    else:
        final_query = search_query

    # 4. Open browser
    if not open_browser():
        return "fail"

    # 5. Wait for browser to be ready
    wait_for_a_number_of_seconds(2)

    # 6. Type the search text
    type_text_exactly(final_query)

    # 7. Press Enter
    press_a_key(Key.enter)

    return "success"
# REACH Language Definitions
# Centralized vocabulary for wake words and command interpretation

# Wake Word Synonyms
WAKE_WORDS = {
    "search": [
        "search",
        "search for",
        "find",
        "look up",
        "look for",
        "google",
        "check",
        "search the web",
        "find information",
        "find me",
        "show me"
    ],

    "ask": [
        "ask",
        "question",
        "explain",
        "tell me",
        "what is",
        "what are",
        "how",
        "how do",
        "how does",
        "why",
        "why is",
        "why does",
        "help me understand",
        "can you explain"
    ],

    "control": [
        "control",
        "media",
        "audio",
        "sound",
        "volume",
        "playback",
        "music control"
    ],

    "navigate": [
        "navigate",
        "go",
        "scroll",
        "move",
        "open",
        "zoom",
        "back",
        "forward",
        "browse",
        "page control"
    ],

    "communicate": [
        "communicate",
        "message",
        "send",
        "send message",
        "text",
        "dm",
        "tell",
        "write to",
        "send to",
        "contact"
    ]
}

# Control Commands

CONTROL_COMMANDS = {
    "play_pause": [
        "pause", "play", "resume",
        "start playback", "stop playback",
        "toggle playback"
    ],
    "tab": [
        "press tab", "tab", "switch field", "next field", "next result"
    ],

    "mute": [
        "mute", "silence", "turn off sound"
    ],

    "unmute": [
        "unmute", "turn sound on"
    ],

    "volume_up": [
        "volume up", "louder", "increase volume",
        "turn it up", "raise volume", "up"
    ],

    "volume_down": [
        "volume down", "quieter", "lower volume",
        "turn it down", "reduce volume", "down"
    ],

    "next_video": [
        "next", "skip", "next video", "next song"
    ],

    "next": [
        "next video", "next track", "next song", "skip"
    ]
}

# Navigation Commands

NAVIGATE_COMMANDS = {
    "scroll_up": ["scroll up", "go up", "page up", "up"],
    "scroll_down": ["scroll down", "go down", "page down", "down"],
    "zoom_in": ["zoom in", "make bigger", "enlarge", "in"],
    "zoom_out": ["zoom out", "make smaller", "shrink", "out"],
    "back": ["go back", "back", "previous page"],
    "forward": ["go forward", "forward"],
    "open_first": [
        "open first result",
        "open the first result",
        "click first result",
        "first result"
    ],
        "tab": [
        "press tab", "tab", "switch field", "next field", "next result"
    ],
    "enter": ["enter", "submit", "confirm"],
    "type": ["type", "write", "input"]

}

# Helper Prefixes

SEARCH_SYNONYMS = [
    "search",
    "search for",
    "find",
    "look up",
    "look for",
    "google",
    "check",
    "show me"
]

ASK_PREFIXES = [
    "ask",
    "ask chatgpt",
    "question",
    "explain",
    "tell me",
    "can you",
    "help me"
]

COMMUNICATE_PREFIXES = [
    "communicate",
    "message",
    "send",
    "send message",
    "text",
    "dm",
    "tell",
    "write to",
    "send to",
    "discord"
]

# Question Detection

QUESTION_WORDS = [
    "what",
    "why",
    "how",
    "when",
    "where",
    "who",
    "which",
    "can",
    "could",
    "should",
    "would",
    "is",
    "are",
    "do",
    "does",
    "did"
]

# Utility Functions

def normalize_text(text: str) -> str:
    return text.lower().strip()


def match_phrase(text: str, phrase_list):
    text = normalize_text(text)
    for phrase in phrase_list:
        if phrase in text:
            return True
    return False


def strip_prefix(text, phrases):
    for phrase in phrases:
        if text.startswith(phrase + " "):
            return text[len(phrase) + 1:].strip()
        if text == phrase:
            return ""
    return text


def looks_like_question(text):
    text = text.strip()

    if text.endswith("?"):
        return True

    first_word = text.split(" ")[0]
    return first_word in QUESTION_WORDS

# Intent Detection

def get_wake_word(text: str):
    """
    Natural language intent detection.
    Returns: (intent, content)
    """

    original_text = text.strip()
    text_lower = normalize_text(text)

    # ---- 1. SEARCH (highest priority for explicit search terms) ----
    if match_phrase(text_lower, WAKE_WORDS["search"]):
        content = strip_prefix(text_lower, WAKE_WORDS["search"])
        if content:
            return "search", content
        return "search", original_text

    # ---- 2. COMMUNICATE (before ASK to avoid conflicts with question words) ----
    if match_phrase(text_lower, WAKE_WORDS["communicate"]):
        content = strip_prefix(text_lower, WAKE_WORDS["communicate"])
        return "communicate", content

    # ---- 3. ASK ----
    if looks_like_question(text_lower):
        return "ask", original_text

    if match_phrase(text_lower, WAKE_WORDS["ask"]):
        content = strip_prefix(text_lower, WAKE_WORDS["ask"])
        if content:
            return "ask", content
        return "ask", original_text

    # ---- 4. CONTROL ----
    if match_phrase(text_lower, WAKE_WORDS["control"]):
        content = strip_prefix(text_lower, WAKE_WORDS["control"])
        return "control", content

    # ---- 5. NAVIGATE ----
    if match_phrase(text_lower, WAKE_WORDS["navigate"]):
        content = strip_prefix(text_lower, WAKE_WORDS["navigate"])
        return "navigate", content

    # ---- 6. Fallback Intelligence ----

    if any(word in text_lower for word in [
        "scroll", "zoom", "back", "forward", "open", "enter"
    ]):
        return "navigate", text_lower

    if any(word in text_lower for word in [
        "volume", "mute", "pause", "play", "skip"
    ]) or "next video" in text_lower:
        return "control", text_lower

    # Default informational query → search
    if len(text_lower.split()) >= 3:
        return "search", text_lower

    return "fail", ""
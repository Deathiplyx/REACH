# This script extracts a website name from phrases like:
# "youtube for funny cats"
# and returns a Google site parameter:
# -> site:youtube.com
#
# If the site is unknown, it falls back to .com

SITE_DOMAINS = {
    # Major platforms
    "youtube": "youtube.com",
    "google": "google.com",
    "gmail": "mail.google.com",
    "drive": "drive.google.com",
    "docs": "docs.google.com",
    "maps": "maps.google.com",
    "calendar": "calendar.google.com",
    "scholar": "scholar.google.com",

    # Education / research
    "wikipedia": "wikipedia.org",
    "khan": "khanacademy.org",
    "khanacademy": "khanacademy.org",
    "coursera": "coursera.org",
    "edx": "edx.org",
    "jstor": "jstor.org",

    # Social / community
    "reddit": "reddit.com",
    "twitter": "twitter.com",
    "x": "twitter.com",
    "facebook": "facebook.com",
    "instagram": "instagram.com",
    "tiktok": "tiktok.com",
    "linkedin": "linkedin.com",
    "discord": "discord.com",

    # Developer / tech
    "github": "github.com",
    "gitlab": "gitlab.com",
    "stackoverflow": "stackoverflow.com",
    "stackexchange": "stackexchange.com",
    "pypi": "pypi.org",
    "npm": "npmjs.com",

    # Media / streaming
    "netflix": "netflix.com",
    "hulu": "hulu.com",
    "prime": "primevideo.com",
    "primevideo": "primevideo.com",
    "spotify": "spotify.com",
    "soundcloud": "soundcloud.com",
    "twitch": "twitch.tv",

    # Shopping
    "amazon": "amazon.com",
    "ebay": "ebay.com",
    "etsy": "etsy.com",
    "walmart": "walmart.com",
    "target": "target.com",
    "bestbuy": "bestbuy.com",

    # Productivity / tools
    "notion": "notion.so",
    "slack": "slack.com",
    "trello": "trello.com",
    "zoom": "zoom.us",
    "dropbox": "dropbox.com",

    # School-specific common LMS
    "canvas": "instructure.com",
    "blackboard": "blackboard.com",
    "moodle": "moodle.org"
}


def run(text):
    text = text.lower()

    # Expect format: "<site> for <query>"
    if "for" not in text:
        return "fail"

    # Extract site name
    website_name = text.split("for", 1)[0].strip()

    # Normalize (remove spaces)
    website_key = website_name.replace(" ", "")

    # Look up domain
    domain = SITE_DOMAINS.get(website_key)

    # Fallback
    if not domain:
        domain = f"{website_key}.com"

    return f"site:{domain}"

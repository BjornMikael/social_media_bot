import json
from handlers.twitter_handler import TwitterHandler
from handlers.mastodon_handler import MastodonHandler

# Load new configuration
with open("config.json", "r") as config_file:
    config = json.load(config_file)

# Initialize handlers
twitter = TwitterHandler(config["twitter"])
mastodon = MastodonHandler(config["mastodon"])

# Example usage
def post_to_all_platforms(message):
    twitter.post(message)
    mastodon.post(message)

if __name__ == "__main__":
    post_to_all_platforms("Hello from my modular bot! 🌍")

import time

while True:
    # Your bot's main logic here
    print("Bot is running...")
    
    # Avoid high CPU usage
    time.sleep(30)  # Wait 30 seconds before running again

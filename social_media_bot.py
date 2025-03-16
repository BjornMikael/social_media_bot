import logging
import time
import json
from handlers.twitter_handler import TwitterHandler
from handlers.mastodon_handler import MastodonHandler

# Configure logging with timestamps
logging.basicConfig(
    filename="bot_output.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Load configuration
with open("config.json", "r") as config_file:
    config = json.load(config_file)

# Initialize handlers
twitter = TwitterHandler(config["twitter"])
mastodon = MastodonHandler(config["mastodon"])

# Function to post a message to all platforms
def post_to_all_platforms(message):
    logging.info("Posting message: %s", message)
    
    if config["twitter"]["enabled"]:
        twitter.post(message)
    else:
        logging.info("Twitter posting is disabled.")
    
    if config["mastodon"]["enabled"]:
        mastodon.post(message)
    else:
        logging.info("Mastodon posting is disabled.")

if __name__ == "__main__":
    logging.info("Bot started.")

    while True:
        post_to_all_platforms("Hello from my modular bot! ^=^l^m")
        logging.info("Bot is running...")

        # Avoid high CPU usage
        time.sleep(30)  # Wait 30 seconds before running again

import json
from handlers.twitter_handler import TwitterHandler

# Load configuration
with open("config.json", "r") as config_file:
    config = json.load(config_file)

# Initialize Twitter handler
twitter = TwitterHandler(config["twitter"])

# Verify credentials
twitter.verify_credentials()

# Example usage
def post_to_twitter(message):
    twitter.post(message)

if __name__ == "__main__":
    post_to_twitter("Hello from my modular bot! 🌍")
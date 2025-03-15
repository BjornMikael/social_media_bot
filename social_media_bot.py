import json
from handlers.twitter_handler import TwitterHandler

# Load configuration
with open("config.json", "r") as config_file:
    config = json.load(config_file)

# Initialize handlers
twitter = TwitterHandler(config["twitter"])

# Example usage
def post_to_twitter(message):
    twitter.post(message)

if __name__ == "__main__":
    post_to_twitter("Hello from my modular bot! 🌍")
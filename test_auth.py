# test_auth.py

from handlers.twitter_handler import TwitterHandler
import json

# Load configuration
with open("config.json", "r") as f:
    config = json.load(f)

# Test authentication
twitter = TwitterHandler(config["twitter"])
twitter.verify_credentials()
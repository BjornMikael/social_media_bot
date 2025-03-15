# handlers/mastodon_handler.py
from mastodon import Mastodon

class MastodonHandler:
    def __init__(self, config):
        self.client = Mastodon(
            access_token=config["access_token"],
            api_base_url=config["api_base_url"]
        )
        self.enabled = config.get("enabled", True)  # Default to True if not specified

    def post(self, message):
        if not self.enabled:
            print("Mastodon posting is disabled.")
            return
        try:
            self.client.toot(message)
            print(f"Mastodon toot published: {message}")
        except Exception as e:
            print(f"Error posting to Mastodon: {e}")
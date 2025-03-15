import tweepy

class TwitterHandler:
    def __init__(self, config):
        self.client = tweepy.Client(
            consumer_key=config["api_key"],
            consumer_secret=config["api_secret"],
            access_token=config["access_token"],
            access_token_secret=config["access_token_secret"]
        )

    def post(self, message):
        try:
            response = self.client.create_tweet(text=message)
            print(f"Tweet posted: {response.data['text']}")
        except tweepy.TweepyException as e:
            print(f"Error posting tweet: {e}")
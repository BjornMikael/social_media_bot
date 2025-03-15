import tweepy
import time
from config import API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

# Authenticate to Twitter
client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

def post_tweet(message):
    try:
        response = client.create_tweet(text=message)
        print(f"Tweet posted: {response.data['text']}")
    except tweepy.TweepyException as e:
        print(f"Error posting tweet: {e}")

if __name__ == "__main__":
    # Example usage
    post_tweet("Hello from my Raspberry Pi bot! 🤖")
    # Add scheduling logic here if needed
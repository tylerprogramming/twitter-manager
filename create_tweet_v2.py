import os
from requests_oauthlib import OAuth1Session
import time

class TweetPoster:
    def __init__(self):
        self.oauth = self._get_oauth_session()
        self.tweet_url = "https://api.twitter.com/2/tweets"

    def _get_oauth_session(self):
        consumer_key = os.environ.get("CONSUMER_KEY")
        consumer_secret = os.environ.get("CONSUMER_SECRET")
        access_token = os.environ.get("ACCESS_TOKEN")
        access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

        # Create the final OAuth1Session
        oauth = OAuth1Session(
            consumer_key,
            client_secret=consumer_secret,
            resource_owner_key=access_token,
            resource_owner_secret=access_token_secret,
        )
        
        return oauth

    def post_tweet(self, tweet_text):
        if not self.oauth:
            return None

        payload = {"text": tweet_text}
        response = self.oauth.post(self.tweet_url, json=payload)

        if response.status_code == 201:
            print("Tweet posted successfully!")
            return response.json()
        else:
            print(f"Failed to post tweet. Status code: {response.status_code}")
            print(response.text)
            return None

if __name__ == "__main__":
    poster = TweetPoster()
    poster.post_tweet("Hello, Twitter! This is a test tweet from my Python script.")
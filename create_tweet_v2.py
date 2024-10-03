from requests_oauthlib import OAuth1Session
import os
import json
from dotenv import load_dotenv

class TweetPoster:
    def __init__(self):
        load_dotenv()
        self.consumer_key = os.environ.get("CONSUMER_KEY")
        self.consumer_secret = os.environ.get("CONSUMER_SECRET")
        self.access_token = os.environ.get("ACCESS_TOKEN")
        self.access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")
        self.bearer_token = os.environ.get("BEARER_TOKEN")
        self.oauth = self._create_oauth_session()

    def _create_oauth_session(self):
        return OAuth1Session(
            self.consumer_key,
            client_secret=self.consumer_secret,
            resource_owner_key=self.access_token,
            resource_owner_secret=self.access_token_secret,
        )

    def post_tweet(self, tweet_text):
        payload = {"text": tweet_text}
        response = self.oauth.post(
            "https://api.twitter.com/2/tweets",
            json=payload,
        )

        if response.status_code != 201:
            raise Exception(
                f"Request returned an error: {response.status_code} {response.text}"
            )

        print(f"Response code: {response.status_code}")
        json_response = response.json()
        print(json.dumps(json_response, indent=4, sort_keys=True))
        return json_response

# Example usage:
if __name__ == "__main__":
    tweet_poster = TweetPoster()
    tweet_text = "👉 Hello world!\n👉 This is a test tweet.\n👉 https://x.com/xmanager\n👉 https://youtu.be/76h5Hq6dTpk"
    tweet_poster.post_tweet(tweet_text)
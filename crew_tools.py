import emoji
from crewai_tools import BaseTool
from create_tweet_v2 import TweetPoster

class TweetManagerTool(BaseTool):
    name: str = "Tweet Manager"
    description: str = "Post a tweet to X (formerly Twitter)."

    def _run(self, tweet: str) -> str:
        tweet_poster = TweetPoster()
        response = tweet_poster.post_tweet(tweet)

        print(f"Tweet: {tweet}")
        print(f"Response: {response.status_code}")

        if 200 <= response.status_code < 300:
            return response
        else:
            raise Exception(f"Failed to post tweet. Status code: {response.status_code}, Response: {response.text}")
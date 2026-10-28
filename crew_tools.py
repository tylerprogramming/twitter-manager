from crewai.tools import BaseTool
from create_tweet_v2 import TweetPoster

class TweetManagerTool(BaseTool):
    name: str = "Tweet Manager"
    description: str = "Post a tweet to X (formerly Twitter)."

    def _run(self, tweet: str) -> str:
        tweet_poster = TweetPoster()
        # post_tweet returns the parsed JSON body on HTTP 201, or None after
        # printing the status code and error body.
        result = tweet_poster.post_tweet(tweet)

        print(f"Tweet: {tweet}")

        if result is None:
            raise Exception("Failed to post tweet. See the status code and response printed above.")

        tweet_id = (result.get("data") or {}).get("id", "unknown")
        return f"Posted tweet {tweet_id}: {tweet}"
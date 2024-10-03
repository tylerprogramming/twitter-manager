import emoji
from crewai_tools import BaseTool
from create_tweet_v2 import TweetPoster

class TweetManagerTool(BaseTool):
    name: str = "Tweet Manager"
    description: str = "Post a tweet to X (formerly Twitter)."

    def _run(self, tweet_data: dict) -> str:
        # Extract the tweet from the dictionary
        tweet = tweet_data.get('tweet', '')

        # Convert emoji aliases to Unicode
        tweet_with_emojis = emoji.emojize(tweet, language='alias')
        
        # Encode the tweet as UTF-8, replacing any problematic characters
        encoded_tweet = tweet_with_emojis.encode('utf-8', errors='replace').decode('utf-8')

        response = TweetPoster().post_tweet(encoded_tweet)
        
        return response
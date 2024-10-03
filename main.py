from twitter_manager_crew import TwitterManagerCrew
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

def run_crew():
    inputs = {
        'topic': 'latest ai news',
        'date': datetime.now().strftime("%Y-%m-%d")
    }

    result = TwitterManagerCrew().crew().kickoff(inputs=inputs)
    print(result)
    
run_crew()
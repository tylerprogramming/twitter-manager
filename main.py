from twitter_manager_crew import TwitterManagerCrew
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

def run_crew():
    inputs = {
        'topic': 'random animal facts',
        'date': datetime.now().strftime("%Y")
    }

    result = TwitterManagerCrew().crew().kickoff(inputs=inputs)
    print(result)
    
run_crew()
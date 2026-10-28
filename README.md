# twitter-manager

A CrewAI crew that finds a recent animal fact, writes a tweet about it, and posts it to X
(formerly Twitter). Five agents run in sequence: retrieve facts with Serper search, pick one,
read the source page, write the tweet, and post it.

## Setup

Python 3.10-3.13.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Fill in `.env`:

- `OPENAI_API_KEY` for the agents' LLM
- `SERPER_API_KEY` for the search tool ([serper.dev](https://serper.dev))
- `CONSUMER_KEY`, `CONSUMER_SECRET`, `ACCESS_TOKEN`, `ACCESS_TOKEN_SECRET` from an
  [X developer app](https://developer.x.com/en/portal/dashboard) with read and write permission

## Run

```bash
python main.py
```

This posts a real tweet to the account that owns the access token. To test the X credentials on
their own, `python create_tweet_v2.py` posts a single hello-world tweet.

Change the topic in `main.py` (`'topic': 'random animal facts'`) and the agent and task prompts
in `config/agents.yaml` and `config/tasks.yaml`.

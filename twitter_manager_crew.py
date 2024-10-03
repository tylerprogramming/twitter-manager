from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from pydantic import BaseModel, Field
from typing import List, Optional
from crew_tools import TweetManagerTool

class Tweet(BaseModel):
    tweet: str = Field(..., description="The tweet to be posted")

@CrewBase
class TwitterManagerCrew():
    """Twitter Manager Crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def ai_news_retriever(self) -> Agent:
        return Agent(
            config=self.agents_config['ai_news_retriever'],
            tools=[SerperDevTool()],
            verbose=True,
            allow_delegation=False,
        )
    
    @agent
    def ai_news_picker(self) -> Agent:
        return Agent(
            config=self.agents_config['ai_news_picker'],
            tools=[],
            verbose=True,
            allow_delegation=False,
        )
    
    @agent
    def ai_news_aggregator(self) -> Agent:
        return Agent(
            config=self.agents_config['ai_news_aggregator'],
            tools=[ScrapeWebsiteTool()],
            verbose=True,
            allow_delegation=False,
        )
    
    @agent
    def tweet_preparer(self) -> Agent:
        return Agent(
            config=self.agents_config['tweet_preparer'],
            tools=[],
            verbose=True,
            allow_delegation=False,
        )
    
    @agent
    def tweet_poster(self) -> Agent:
        return Agent(
            config=self.agents_config['tweet_poster'],
            tools=[TweetManagerTool()],
            verbose=True,
            allow_delegation=False,
        )
    
    @task
    def ai_news_retrieval_task(self) -> Task:
        return Task(
            config=self.tasks_config['ai_news_retrieval_task'],
            agent=self.ai_news_retriever(),
        )
    
    @task
    def ai_news_picker_task(self) -> Task:
        return Task(
            config=self.tasks_config['ai_news_picker_task'],
            agent=self.ai_news_picker(),
        )
    
    @task
    def ai_news_aggregation_task(self) -> Task:
        return Task(
            config=self.tasks_config['ai_news_aggregation_task'],
            agent=self.ai_news_aggregator(),
        )
    
    @task
    def tweet_preparation_task(self) -> Task:
        return Task(
            config=self.tasks_config['tweet_preparation_task'],
            agent=self.tweet_preparer(),
        )
    
    @task
    def tweet_posting_task(self) -> Task:
        return Task(
            config=self.tasks_config['tweet_posting_task'],
            agent=self.tweet_poster(),
            output_json=Tweet
        )

    @crew
    def crew(self) -> Crew:
        """Creates a Twitter Manager Crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
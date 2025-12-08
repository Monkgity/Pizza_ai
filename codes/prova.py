

from datapizza.agents import Agent
from datapizza.clients.openai import OpenAIClient
from datapizza.tools import tool

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__),'..','.env')
print(dotenv_path)
load_dotenv(dotenv_path)

OPENAI_KEY = os.environ.get("OPENAI_KEY")
print(OPENAI_KEY)


@tool
def get_weather(city: str) -> str:
    return f"The weather in {city} is sunny"

client = OpenAIClient(api_key=OPENAI_KEY)
agent = Agent(name="assistant", client=client, tools = [get_weather])

response = agent.run("What is the weather in Rome?")
# output: The weather in Rome is sunny

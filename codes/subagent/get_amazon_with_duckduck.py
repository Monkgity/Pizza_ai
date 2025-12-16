import base64
from openai import OpenAI
import os
from os.path import join, dirname
from dotenv import load_dotenv
from datapizza.clients.openai import OpenAIClient
from datapizza.tools import tool
from datapizza.agents import Agent
from openai import OpenAI
import yaml

from datapizza.tools.duckduckgo import DuckDuckGoSearchTool

dotenv_path = join(dirname(__file__),'..','..','.env')
cfg_path = join(dirname(__file__),'..','..','config.yaml')
load_dotenv(dotenv_path)
with open(cfg_path) as f:
    cfg = yaml.safe_load(f)


OPENAI_KEY = os.environ.get("OPENAI_KEY")
AMAZON_AGENT = cfg["AMAZON_DUCK"]
system_prompt = cfg["duck_agent_prompt"]

client = OpenAIClient(api_key=OPENAI_KEY, model=AMAZON_AGENT)

web_search_agent = Agent(
    name="web_search_expert",
    client=client,
    system_prompt=system_prompt,
    tools=[DuckDuckGoSearchTool()])


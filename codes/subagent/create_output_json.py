import base64
from openai import OpenAI
import os
from os.path import join, dirname
from dotenv import load_dotenv
from datapizza.clients.openai import OpenAIClient
from datapizza.tools import tool
from datapizza.agents import Agent
import yaml

dotenv_path = join(dirname(__file__),'..','..','.env')
cfg_path = join(dirname(__file__),'..','..','config.yaml')
load_dotenv(dotenv_path)
with open(cfg_path) as f:
    cfg = yaml.safe_load(f)


OPENAI_KEY = os.environ.get("OPENAI_KEY")
JSON_AGENT = cfg["JSON_AGENT"]

system_prompt = cfg["Json_Agent"]
client = OpenAIClient(api_key=OPENAI_KEY, model=JSON_AGENT)

json_agent = Agent(
    name="json_expert",
    client=client,
    system_prompt=system_prompt)
    
    

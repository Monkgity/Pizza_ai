#----------------------------------   SUBAGENTS   ----------------------------------------------------#

from codes.subagent.get_amazon_with_duckduck import web_search_agent
from codes.subagent.create_output_json import json_agent

#---------------------------------- TOOL -------------------------------------------------------------#

from codes.tool.get_photo_info_openai import get_photo_info 
from codes.tool.get_post_from_insta import get_post

#--------------------------------- LIBRARIES ---------------------------------------------------------#

from datapizza.clients.openai import OpenAIClient

from datapizza.agents import Agent,StepResult
from datapizza.tools import tool

from os.path import join, dirname
from typing import List,Dict
from dotenv import load_dotenv
import sys, os
import base64
import json
import yaml

#---------------------------------  VARIABLES  ------------------------------------------------#
dotenv_path = join(dirname(__file__),'.env')
load_dotenv(dotenv_path)
OPENAI_KEY = os.environ.get("OPENAI_KEY")

cfg_path = join(dirname(__file__),'config.yaml')
with open(cfg_path) as f:
    cfg = yaml.safe_load(f)

#--------------------------------- MAIN AGENT PIZZAAAAAAAAAAAAAA ------------------------------------#

def main_agent_call(person:str, budget:int) -> str:

    ### CONFIGURAZIONE AGENTE
    MAIN_AGENT = cfg["MAIN_AGENT"]
    client = OpenAIClient(api_key=OPENAI_KEY, model = MAIN_AGENT)    

    ### INIZIALIZZAZIONE AGENTE
    main_agent = Agent(name="Assistant_GIFT",
                   system_prompt = cfg["main_agent_prompt"] , 
                   client = client,
                   tools = [get_post,get_photo_info])
        
    messaggio = f"Ciao cosa posso regalare a questa persona : {person} con questo {budget}"
    main_agent.can_call([web_search_agent,json_agent])

    response = main_agent.run(messaggio)  # ritorna un json con nome, descrizione, info, links
    response = response.text  

    # spezzo gli agenti per sicurezza output
    risposta_json = json_agent.run(response)  
    risposta_json = risposta_json.text
    
    print(risposta_json)
    json_answer = json.loads(risposta_json)
    print(json_answer)

    return response, json_answer



if __name__ == "__main__":
    PERSON = "inserisci profilo"
    BUDGET = 20
    risposta,risposta_json = main_agent_call(PERSON,BUDGET)


    print("ANSWER AGENT")
    print(risposta)

    print("RISPSOTA JSON")
    print(risposta_json)

    try:
        json_answer = json(risposta_json)
        print("formattazione riuscita")
        print(json_answer)
    except Exception as E:
        print(f"errore in convertire in json per {E}")
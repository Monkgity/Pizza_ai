import http.client
from os.path import join, dirname
import os
from dotenv import load_dotenv
import sys
import json
import yaml
from typing import List,Dict
from datapizza.clients.openai import OpenAIClient
from datapizza.tools import tool
from datapizza.agents import Agent


dotenv_path = join(dirname(__file__),'..','..','.env')
load_dotenv(dotenv_path)
CHIAVE_INSTA = os.environ.get("CHIAVE_INSTA")

cfg_path = join(dirname(__file__),'..','..','config.yaml')
with open(cfg_path) as f:
    cfg = yaml.safe_load(f)

MAX_PHOTO_FOR_PROFILE = cfg["max_photo_for_profile"]

@tool
def get_post(account: str) -> Dict:


    """
    prende di input un singolo account instagram e tramite chiamate api ritorna una lsita di url che sono le foto
    è importante passare solo i nomi per interi, togli sempre l url lasciando solo il nome dell utente
    Esempio di chiamata:
    get_post("marcoschiavo__")

    """
    conn = http.client.HTTPSConnection("instagram120.p.rapidapi.com")
    headers = {
        'x-rapidapi-key': f"{CHIAVE_INSTA}",
        'x-rapidapi-host': "instagram120.p.rapidapi.com",
        'Content-Type': "application/json"
    }


    payload = "{\"username\":\"" + str(account) + "\"}"
    conn.request("POST", "/api/instagram/posts", payload, headers)
    res = conn.getresponse()
    data = res.read()
    data = data.decode("utf-8")

    NUMERO_MAX_DI_FOTO = MAX_PHOTO_FOR_PROFILE


    foto: List = []
    dizio = json.loads(data)
    lista_di_post = dizio["result"]["edges"]
    for post in lista_di_post:
        try:
            element = post
            element1 = element["node"]["image_versions2"]["candidates"][0]["url"]   # prima foto di ogni psot
            foto.append(element1)
            element2 = element["node"]["carousel_media"]
            if(element2):
                for sub_phot in element2:
                    subphoto = sub_phot["image_versions2"]["candidates"][0]["url"]   # sotto foto del post
                    foto.append(subphoto)
        except Exception as E:
            print("Qualsiasi errore, probabilmente non ha post o solo video")

    try:    
        prime_foto = foto[:NUMERO_MAX_DI_FOTO]
    except Exception as E:
        print(f"ERRORREEEEEE! no serio il motivo è: {E}")
        prime_foto = foto
    
    return str(prime_foto)

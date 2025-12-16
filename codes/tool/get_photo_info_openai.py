from os.path import join, dirname
from datapizza.tools import tool
from dotenv import load_dotenv
from openai import OpenAI
from typing import List
from PIL import Image

import urllib.request
import requests
import base64
import yaml
import os

dotenv_path = join(dirname(__file__),'..','..','.env')
cfg_path = join(dirname(__file__),'..','..','config.yaml')
load_dotenv(dotenv_path)
with open(cfg_path) as f:
    cfg = yaml.safe_load(f)


OPENAI_KEY = os.environ.get("OPENAI_KEY")
PHOTO_AGENT = cfg["PHOTO_AGENT"]


PROMPT = """
You are a helpful assistant that analyzes photos and provides info about the scenario, 
find any hobbies or interests of the person in the photo the final point be fast and add a small description of the foto and 2,3 ideas of gifts
Example foto: ..
Output ; i see a beach and people playing volley, you can buy them a volleyball ball or a volleyball net
"""

@tool
def get_photo_info(lista_di_foto: List[str] ) -> str:
    client = OpenAI(api_key=OPENAI_KEY)


    """
    prende di input una lista con dentro una di url di foto e ritorna una stringa con info sui
    possibili regali in base agli interessi
    """
    interessi_della_persona = ""

    def get_as_base64(url):
        return base64.b64encode(requests.get(url).content).decode('utf-8')
        
    for foto in lista_di_foto: 
        url_foto = foto
        try:
            base64_image = get_as_base64(url_foto)

            completion = client.chat.completions.create(
                model="gpt-4.1",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            { "type": "text", "text": f"{PROMPT}"},
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{base64_image}",
                                },
                            },
                        ],
                    }
                ],
            )
            interessi_della_persona += completion.choices[0].message.content   
        except:
            interessi_della_persona = interessi_della_persona
    return interessi_della_persona
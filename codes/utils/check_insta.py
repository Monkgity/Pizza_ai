import http.client
import os
import json
from os.path import join, dirname
from dotenv import load_dotenv
from typing import List

# Carica la chiave dall'.env
dotenv_path = join(dirname(__file__), '..', '..', '.env')
load_dotenv(dotenv_path)
CHIAVE_INSTA = os.environ.get("CHIAVE_INSTA")


def check_insta(account: str) -> str:
    """
    Ritorna solo lo stato della lettura di un account Instagram.
    Possibili valori:
    - "INSERISCI CHIAVE"   -> chiave API mancante o non valida
    - "PAGINA PRIVATA"     -> account privato
    - "ERRORE LETTURA"     -> errore generico nella chiamata o parsing
    - "OK"                 -> account letto correttamente
    """

    # Caso chiave mancante
    if not CHIAVE_INSTA:
        return "INSERISCI CHIAVE"

    try:
        conn = http.client.HTTPSConnection("instagram120.p.rapidapi.com")
        headers = {
            'x-rapidapi-key': CHIAVE_INSTA,
            'x-rapidapi-host': "instagram120.p.rapidapi.com",
            'Content-Type': "application/json"
        }

        payload = json.dumps({"username": account})
        conn.request("POST", "/api/instagram/posts", payload, headers)
        res = conn.getresponse()
        data = res.read().decode("utf-8")
        dizio = json.loads(data)

        # Caso chiave non valida
        if dizio == {'message': 'You are not subscribed to this API.'}:
            return "INSERISCI CHIAVE"
        print(account)
        print(dizio)
        # Caso account privato
        if "message" in dizio:
            if(dizio["message"] == 'This page is private'):
                return "PAGINA PRIVATA"

        # Caso account letto bene (se ha la chiave "result")
        if "result" in dizio and "edges" in dizio["result"]:
            return "OK"

        # Qualsiasi altro caso
        return "ERRORE LETTURA"

    except Exception:
        return "ERRORE LETTURA"
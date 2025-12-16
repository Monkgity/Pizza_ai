# 🎄 ELFI AI
### Il modo più semplice (e meno stressante) per scegliere regali di Natale usando l’AI

Scegliere i regali è sempre la stessa storia:  
idee poche, tempo zero e ansia alle stelle.

**ELFI AI** nasce per risolvere questo problema sfruttando **agenti AI** e un workflow automatizzato basato sul framework **Datapizza**.  
Tu fornisci un **profilo Instagram** e un **budget**, gli elfi analizzano i contenuti social e generano suggerimenti regalo coerenti, utili e (si spera) azzeccati.

Meno stress per te, più lavoro per gli elfi 🤖🎁

---

## 🧠 Come funziona

Il progetto utilizza:
- **Agenti AI** configurabili tramite un config
- Analisi di **post e foto Instagram**
- Integrazione con **OpenAI** per analisi delle foto
- Ricerca automatica di prodotti (es. Amazon)
- Output strutturato in JSON
- Interfaccia web tramite **Streamlit**

Il tutto è orchestrato tramite **Datapizza**, che gestisce il workflow degli agenti.

---

## 📁 Struttura del progetto

```text
.
├── main.py
├── config.yaml
├── requirments.txt
├── .gitignore
├── .env
├── codes
│   ├── subagent
│   │   ├── create_output_json.py
│   │   └── get_amazon_link_with_duckduck.py
│   └── tools
│       ├── get_photo_info_openai.py
│       └── get_post_from_insta.py
└── streamlit
    └── streamlit_main.py
```

1.  **Clona il repository:**
    ```bash
    git clone https://github.com/Monkgity/Pizza_ai.git
    cd Pizza_ai
    ```

2.  **Crea e attiva l'environment:**

    Su macOS/Linux:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

    Su Windows:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Installa le dipendenze:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Inserisci le chiavi tue nell env:**
    ```bash
    OPENAI_KEY = "INSERISCI_LA_TUA_CHAIVE"
    CHIAVE_INSTA = "INSERISCI_LA_TUA_CHAIVE"
    ```


**COME OTTENERE LE CHIAVI:**

per OPENAI    *https://openai.com/api/*        
per INSTAGRAM     *https://rapidapi.com/3205/api/instagram120*  


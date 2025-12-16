import streamlit as st
import base64
import sys, os
from pathlib import Path
path = sys.path.append(os.path.abspath(""))
from codes.utils.check_insta import check_insta
from main import main_agent_call
import json

# ---------- CONFIG ----------
BASE_DIR = Path(__file__).resolve().parent
main_bg = BASE_DIR / "foto" / "img12.png"
main_bg_ext = "png"

def get_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# ---------- STYLES ----------
st.markdown(
    f"""
    <style>
    .stApp {{
        background: url(data:image/{main_bg_ext};base64,{get_base64(main_bg)});
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- INIZIO APP ----------
st.title(":rainbow[ELFI SOCIAL] 🎄")
st.caption("Ciaooo Viaggiatore! Siamo gli elfi che ti aiuteranno a fare il regalo perfetto 🎁")

# Inizializza session_state se non presente
if "budget" not in st.session_state:
    st.session_state["budget"] = None
if "NOME_FINALE" not in st.session_state:
    st.session_state["NOME_FINALE"] = None

# ---------- INPUT ----------
st.subheader("Dammi qualche info sul fortunato")

budget_choice = st.selectbox(
    "Scegli il budget per persona",
    ("5", "10", "15", "20", "30", "40", "vabbe anche basta eh"),
    index=1,
)
budget_val = 50 if budget_choice == "vabbe anche basta eh" else int(budget_choice)
st.session_state["budget"] = budget_val

# Input singolo nome
st.caption("Inserisci username Instagram")

cols = st.columns([3,1])

with cols[0]:
    nome = st.text_input("Inserisci username Instagram", key="nome_unico",label_visibility='collapsed')
with cols[1]:
    if st.button("Check Insta Profile"):
        if nome.strip():
            ans = check_insta(nome.strip())
            if ans == "OK":
                st.success(f"{nome} valido ✅")
                st.session_state["NOME_FINALE"] = nome.strip()
            elif ans == "INSERISCI CHIAVE":
                st.error("⚠️ Chiave API mancante o non valida. Inserisci la chiave per continuare.")
            elif ans == "PAGINA PRIVATA":
                st.warning(f"🔒 La pagina di {nome} è privata")
            elif ans == "ERRORE LETTURA":
                st.error(f"❌ Errore nella lettura del profilo {nome}. Riprova o controlla l'username.")
            else:
                st.error(f"Profilo {nome} non trovato o risposta inattesa.")
        else:
            st.warning("Inserisci un nome prima di controllare.")

# ---------- AVVIO ANALISI ----------
if st.button("AVVIOO ANALISI"):
    if not st.session_state["NOME_FINALE"]:
        st.error("⚠️ Nessun nome valido da analizzare.")
    else:
        with st.spinner("⏳ Analisi in corso... aspetta un attimo!"):
            risposta, risposta_json = main_agent_call([st.session_state["NOME_FINALE"]], budget_val)
            if isinstance(risposta_json, str):
                risposta_json = json.loads(risposta_json)


        # Mostra output in modo carino
        st.success("🎉 Analisi completata!")
        st.balloons()

        st.markdown(f"### 👤 Utente: **{risposta_json['nome_utente']}**")
        st.markdown(f"**Personalità:** {risposta_json['personalita']}")

        st.markdown("### 🎁 Possibili regali:")
        for regalo in risposta_json["possibili_regali"]:
            st.markdown(f"- {regalo}")

        st.markdown("### 🔗 Link utili:")
        for link in risposta_json["links"]:
            st.markdown(f"[{link}]({link})")

        # Palloncini 🎈
        st.balloons()

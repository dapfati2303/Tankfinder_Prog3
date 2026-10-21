import pandas as pd
import streamlit as st
st.set_page_config(page_title="Tankfinder Spike", page_icon="⛽", layout="wide")
from daten import TANKSTELLEN
from funktionen import durchschnittspreise, guenstigste, nur_offene

st.title("Spike: Tankstellen-Preise")

# ---Bedienelememnte ---
with st.sidebar:
    st.header("Flter")
    nur_geoeffnet = st.checkbox("Nur geöffnete Tankstellen")
    hoechstpreis = st.slider("Höchstpreis E5 (€)", 1.90, 2.30, 2.50, step=0.001)

# --- Daten filtern ---
auswahl = TANKSTELLEN
if nur_geoeffnet:
    auswahl = nur_offene(auswahl)
auswahl = [t for t in auswahl if t["e5"] <= hoechstpreis]

# --- Kennzahlen ---
st.metric("Anzahl Tankstellen", len(auswahl))

if auswahl:
    st.metric("Durchschnitt E5", f"{durchschnittspreise(auswahl, 'e5'):.3f} €")
    billig = guenstigste(auswahl, "e5")
    st.metric("Günstigste", billig["name"], f"{billig['e5']:.3f} €")
    tabelle = pd.DataFrame(auswahl)
    st.dataframe(tabelle[["name", "ort", "e5", "offen"]])
    st.map(tabelle.rename(columns={"lng": "lon"}))
else:
    st.warning("Keine Tankstellen gefunden")




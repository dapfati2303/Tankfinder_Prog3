import streamlit as st
from daten import tankstellen_daten
from funktionen import tankstellen_nach_marke_filtern, tankstellen_unter_preislimit

st.title("Tankstellen-Finder")

st.sidebar.header("Filter")

# Marken aus den Daten sammeln und eine "Alle"-Option hinzufügen
marken = ["Alle"] + list(set(s['marke'] for s in tankstellen_daten))
ausgewaehlte_marke = st.sidebar.selectbox("Marke auswählen", marken)

# Schieberegler für den Dieselpreis
max_preis = st.sidebar.slider("Max Preis für Diesel", 1.00, 2.50, 1.80, 0.01)

# Daten filtern
gefilterte_daten = tankstellen_daten.copy()

if ausgewaehlte_marke != "Alle":
    gefilterte_daten = tankstellen_nach_marke_filtern(gefilterte_daten, ausgewaehlte_marke)

gefilterte_daten = tankstellen_unter_preislimit(gefilterte_daten, "Diesel", max_preis)

# Ergebnisse anzeigen
st.header("Gefundene Tankstellen")
if gefilterte_daten:
    for station in gefilterte_daten:
        st.write(f"**{station['name']}** ({station['marke']}) - Diesel: {station['Diesel']}€")
    else:
        st.write("Keine Tankstellen gefunden, die den Kriterien entsprechen.")

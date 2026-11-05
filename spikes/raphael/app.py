import html
import json

import streamlit as st
import streamlit.components.v1 as components

from daten import TANKSTELLEN
from funktionen import KRAFTSTOFFE, guenstigste_tankstelle, top_tankstellen


st.set_page_config(page_title="Tankfinder-Karte", page_icon="⛽", layout="wide")
st.title("Tankstellen im Allgäu")
st.caption("Leaflet-Prototyp mit lokalen Testdaten")

kraftstoff = st.selectbox(
    "Kraftstoff auswählen",
    options=list(KRAFTSTOFFE),
    format_func=lambda key: KRAFTSTOFFE[key],
)

guenstigste = guenstigste_tankstelle(TANKSTELLEN, kraftstoff)
top_fuenf = top_tankstellen(TANKSTELLEN, kraftstoff, anzahl=5)

if not top_fuenf:
    st.warning("Für diese Kraftstoffsorte sind keine Preise verfügbar.")
else:
    st.metric(
        f"Günstigste Tankstelle für {KRAFTSTOFFE[kraftstoff]}",
        guenstigste["name"],
        f'{guenstigste[kraftstoff]:.3f} €/Liter',
    )

    st.subheader("Karte")
    stations_json = json.dumps(TANKSTELLEN, ensure_ascii=False).replace("<", "\\u003c")
    map_html = """
    <div id="map"></div>
    <style>
      html, body, #map { height: 100%; margin: 0; }
      .leaflet-popup-content { line-height: 1.5; }
    </style>
    <link rel="stylesheet"
      href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"
      integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY="
      crossorigin=""/>
    <script
      src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"
      integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo="
      crossorigin=""></script>
    <script>
      const stations = __STATIONS_JSON__;
      const fuel = "__FUEL__";
      const fuelLabel = "__FUEL_LABEL__";
      const map = L.map("map").setView([47.65, 10.55], 9);

      L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
        maxZoom: 19,
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
      }).addTo(map);

      function escapeHtml(value) {
        return String(value).replace(/[&<>"']/g, character => ({
          "&": "&amp;", "<": "&lt;", ">": "&gt;",
          '"': "&quot;", "'": "&#39;"
        })[character]);
      }

      stations.forEach(station => {
        const price = station[fuel];
        if (price === null || price === undefined || !Number.isFinite(Number(price))) {
          return;
        }

        const isCheapest = station.id === __CHEAPEST_ID__;
        const marker = L.circleMarker([station.lat, station.lng], {
          radius: isCheapest ? 10 : 7,
          color: isCheapest ? "#176b35" : "#1f5f99",
          fillColor: isCheapest ? "#2ecc71" : "#4da3ff",
          fillOpacity: 0.9,
          weight: 2
        }).addTo(map);

        const address = `${station.street}, ${station.city}`;
        marker.bindPopup(
          `<strong>${escapeHtml(station.name)}</strong>` +
          `${isCheapest ? " <strong>(günstigste)</strong>" : ""}<br>` +
          `${escapeHtml(address)}<br>` +
          `${escapeHtml(fuelLabel)}: ${Number(price).toFixed(3)} €/Liter<br>` +
          `${station.is_open ? "Geöffnet" : "Geschlossen"}`
        );
      });
    </script>
    """
    map_html = (
        map_html.replace("__STATIONS_JSON__", stations_json)
        .replace("__FUEL__", kraftstoff)
        .replace("__FUEL_LABEL__", html.escape(KRAFTSTOFFE[kraftstoff], quote=True))
        .replace("__CHEAPEST_ID__", str(guenstigste["id"]) if guenstigste else "null")
    )
    components.html(map_html, height=500, scrolling=False)
    st.caption("Kartendaten: © OpenStreetMap-Mitwirkende")

    st.subheader("Die fünf günstigsten Tankstellen")
    st.dataframe(
        [
            {
                "Tankstelle": station["name"],
                "Ort": station["city"],
                "Preis (€/Liter)": f'{station[kraftstoff]:.3f}',
                "Status": "Geöffnet" if station["is_open"] else "Geschlossen",
            }
            for station in top_fuenf
        ],
        hide_index=True,
        use_container_width=True,
    )

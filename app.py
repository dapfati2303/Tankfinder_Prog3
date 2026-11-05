"""Flask-Backend für den Tankfinder.

Start (aus dem Wurzelordner des Repos):  python app.py
Danach erreichbar unter:                 http://localhost:5000
API-Beschreibung:                        docs/api.md
"""

import json
from pathlib import Path

import pandas as pd
from flask import Flask, jsonify, request, send_from_directory

from tankfinder.application import APP

BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BASE_DIR / "frontend"
CSV_PATH = BASE_DIR / "data" / "tankstellen.csv"

ERLAUBTE_FUELS = ("e5", "e10", "diesel")

app = Flask(__name__)
app.json.ensure_ascii = False  # Umlaute im JSON lesbar ausgeben


# ---------------------------------------------------------------- Hilfsfunktionen

def fehler(nachricht, status=400):
    """Fehlerantwort nach docs/api.md: {"error": "..."} mit Status 400."""
    return jsonify({"error": nachricht}), status


def lade_stationen():
    """Liest die Tankstellen aus der CSV.

    Übergangslösung: Sobald StationList gemergt ist, hier auf StationList umstellen.
    """
    return pd.read_csv(CSV_PATH)


def parse_bool(wert):
    """'true'/'false' (Groß-/Kleinschreibung egal) -> bool, sonst ValueError."""
    wert = wert.strip().lower()
    if wert == "true":
        return True
    if wert == "false":
        return False
    raise ValueError(wert)


# ---------------------------------------------------------------- Routen

@app.route("/")
def index():
    """Liefert die Startseite des Frontends aus."""
    return send_from_directory(FRONTEND_DIR, "index.html")


@app.route("/api/info")
def info():
    """Projektinformation aus APP.status()."""
    return jsonify({"status": APP.status()})


@app.route("/api/stations")
def stations():
    """Tankstellen, gefiltert nach fuel, open_only und max_price (siehe docs/api.md)."""
    # --- Parameter prüfen ---
    fuel = request.args.get("fuel", "e5").strip().lower()
    if fuel not in ERLAUBTE_FUELS:
        return fehler(f"Unbekannte Spritsorte: {fuel}")

    open_only_text = request.args.get("open_only", "false")
    try:
        open_only = parse_bool(open_only_text)
    except ValueError:
        return fehler(f"Ungültiger Wert für open_only: {open_only_text} (erlaubt: true, false)")

    max_price = None
    max_price_text = request.args.get("max_price")
    if max_price_text is not None:
        try:
            max_price = float(max_price_text.replace(",", "."))
        except ValueError:
            return fehler(f"Ungültiger Wert für max_price: {max_price_text} (Zahl erwartet)")
        if max_price <= 0:
            return fehler("max_price muss größer als 0 sein")

    # --- Daten filtern und sortieren ---
    df = lade_stationen()
    df = df[df[fuel].notna()]
    if open_only:
        df = df[df["is_open"]]
    if max_price is not None:
        df = df[df[fuel] <= max_price]
    df = df.sort_values(fuel)

    # über to_json, damit Zahlen/Wahrheitswerte/NaN sauber in JSON umgewandelt werden
    stationen = json.loads(df.to_json(orient="records", force_ascii=False))

    return jsonify({
        "fuel": fuel,
        "count": len(stationen),
        "stations": stationen,
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)

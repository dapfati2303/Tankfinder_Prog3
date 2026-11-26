"""Zugriff auf die Tankerkönig-API (https://creativecommons.tankerkoenig.de).

Der API-Key wird an genau einer Stelle verwaltet: in der Datei .env im
Wurzelordner des Repos (Vorlage: .env.example). Die echte .env wird nie committet.

Schnelltest (aus dem Wurzelordner):  python -m tankfinder.tankerkoenig
"""

import os
from pathlib import Path

from dotenv import load_dotenv

ENV_PATH = Path(__file__).resolve().parent.parent / ".env"
PLATZHALTER = "dein-api-key-hier"


class TankerkoenigFehler(Exception):
    """Eigene Fehlermeldung für alles rund um die Tankerkönig-API."""


class TankerkoenigClient:
    """Client für die Tankerkönig-API."""

    BASE_URL = "https://creativecommons.tankerkoenig.de/json"
    ENV_VARIABLE = "TANKERKOENIG_API_KEY"

    def __init__(self, api_key):
        if not api_key or not api_key.strip() or api_key.strip() == PLATZHALTER:
            raise TankerkoenigFehler("Ungültiger API-Key: Der Key ist leer oder noch der Platzhalter.")
        self.api_key = api_key.strip()

    @classmethod
    def from_env(cls, env_path=ENV_PATH):
        """Erzeugt einen Client mit dem API-Key aus der .env-Datei."""
        load_dotenv(env_path)
        api_key = os.getenv(cls.ENV_VARIABLE)

        if not api_key or not api_key.strip() or api_key.strip() == PLATZHALTER:
            raise TankerkoenigFehler(
                f"Kein Tankerkönig-API-Key gefunden. "
                f"Kopiere .env.example nach .env und trage dort deinen Key ein: "
                f"{cls.ENV_VARIABLE}=<dein Key>"
            )
        return cls(api_key)

    def __repr__(self):
        """Zeigt nur die letzten 4 Zeichen des Keys, damit er nicht in Logs landet."""
        return f"TankerkoenigClient(api_key='…{self.api_key[-4:]}')"


if __name__ == "__main__":
    try:
        client = TankerkoenigClient.from_env()
        print("API-Key geladen:", client)
    except TankerkoenigFehler as fehler:
        print("Fehler:", fehler)

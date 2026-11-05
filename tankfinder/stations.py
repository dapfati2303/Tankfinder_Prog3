from pathlib import Path
import pandas as pd


class StationList:
    #Klasse, sie verwaltet die Tankstellendaten und stellt sie als Liste zur Verfügung.

    def __init__(self, file_path: str = None):
        #Initialisiert die StationList und lädt die CSV-Daten.
        if file_path is None:
            # Ermittelt den Pfad automatisch relativ zum Projektverzeichnis,
            # egal von wo aus das Skript gestartet wird.
            base_dir = Path(__file__).resolve().parent.parent
            file_path = base_dir / "data" / "tankstellen.csv"

        # CSV-Datei einlesen und in eine Liste von Dicts umwandeln
        df = pd.read_csv(file_path)
        self.stations = df.to_dict(orient="records")

    def get_all(self) -> list:
        """Gibt alle Tankstellen als Liste zurück."""
        return self.stations


# Test-Instanz für die direkte Nutzung im Modul
if __name__ == "__main__":
    station_list = StationList()
    print(f"Erfolgreich geladen: {len(station_list.get_all())} Tankstellen.")
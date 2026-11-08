import pandas as pd

class StationList:
    """Verwaltet eine Liste von Tankstellen aus einer CSV-Datei."""

    def __init__(self, data: pd.DataFrame = None, name: str = "default"):
        self.name = name
        self.data = pd.DataFrame() if data is None else data

    @classmethod
    def from_csv(cls, path: str, name: str = "default") -> "StationList":
        """Lädt Tankstellendaten aus einer CSV-Datei."""
        df = pd.read_csv(path)
        return cls(data=df, name=name)

    def get_all(self) -> list[dict]:
        """Gibt alle Tankstellen als Liste zurück."""
        return self.data.to_dict(orient="records")

if __name__ == "__main__":
    # Test-Instanz für die direkte Nutzung im Modul
    station_list = StationList.from_csv("data/tankstellen.csv")
    print(f"Erfolgreich geladen: {len(station_list.get_all())} Tankstellen.")
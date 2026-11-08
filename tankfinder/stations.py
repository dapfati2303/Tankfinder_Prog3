
import pandas as pd

class StationList:
    """Verwaltet eine Liste von Tankstellen aus einer CSV-Datei."""

    def __init__(self, data: pd.DataFrame = None, name: str = "default"):
        self.name = name
        self.data = pd.DataFrame() if data is None else data

"Step 2: Filter- und Auswertungslogik für StationList ergänzt"
    
@classmethod
def from_csv(cls, path: str, name: str = "default") -> "StationList":
        """Lädt Tankstellendaten aus einer CSV-Datei."""
        df = pd.read_csv(path)
        return cls(data=df, name=name)

def get_all(self) -> list[dict]:
        """Gibt alle Tankstellen als Liste zurück."""
        return self.data.to_dict(orient="records")

def filter_by_brand(self, brand: str) -> "StationList":
        """Filtert Tankstellen nach einer bestimmten Marke."""
        if self.data.empty or "brand" not in self.data.columns:
            return StationList(name=f"{self.name} - filtered by {brand}")
        
        filtered_df = self.data[self.data["brand"].str.lower() == brand.lower()].copy()
        return StationList(data=filtered_df, name=f"{self.name} - filtered by {brand}")

def cheapest(self, fuel: str) -> dict | None:
        """Gibt die günstigste Tankstelle für eine Sorte als Dictionary zurück."""
        if self.data.empty or fuel not in self.data.columns:
            return None
        valid_df = self.data.dropna(subset=[fuel])
        if valid_df.empty:
            return None
        cheapest_row = valid_df.loc[valid_df[fuel].idxmin()]
        return cheapest_row.to_dict()

if __name__ == "__main__":
    # Test-Instanz für die Akzeptanzkriterien
    station_list = StationList.from_csv("data/tankstellen.csv")
    print(f"Erfolgreich geladen: {len(station_list.get_all())} Tankstellen.")
    
    # Test Filter & Günstigste Tankstelle
    filtered = station_list.filter_by_brand("ARAL")
    print(f"Aral Tankstellen: {len(filtered.get_all())}")
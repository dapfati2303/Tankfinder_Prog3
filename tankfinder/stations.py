
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

    def open_only(self) -> "StationList":
        """Gibt eine neue StationList nur mit geöffneten Tankstellen zurück."""
        if self.data.empty or "isOpen" not in self.data.columns:
            return StationList(name=f"{self.name} - open only")
        filtered_df = self.data[self.data["isOpen"] == True].copy()
        return StationList(data=filtered_df, name=f"{self.name} - open only")

    def below_price(self, fuel: str, limit: float) -> "StationList":
        """Filtert Tankstellen, deren Preis unter dem Limit liegt."""
        if self.data.empty or fuel not in self.data.columns:
            return StationList(name=f"{self.name} - below {limit}")
        valid_df = self.data.dropna(subset=[fuel])
        filtered_df = valid_df[valid_df[fuel] < limit].copy()
        return StationList(data=filtered_df, name=f"{self.name} - below {limit}")

    def sorted_by_price(self, fuel: str) -> "StationList":
        """Sortiert die Tankstellen aufsteigend nach dem Preis einer Sorte."""
        if self.data.empty or fuel not in self.data.columns:
            return StationList(name=f"{self.name} - sorted by {fuel}")
        valid_df = self.data.dropna(subset=[fuel])
        sorted_df = valid_df.sort_values(by=fuel).copy()
        return StationList(data=sorted_df, name=f"{self.name} - sorted by {fuel}")

    def mean_price(self, fuel: str) -> float | None:
        """Berechnet den Durchschnittspreis für eine Kraftstoffsorte."""
        if self.data.empty or fuel not in self.data.columns:
            return None
        valid_df = self.data.dropna(subset=[fuel])
        if valid_df.empty:
            return None
        return float(valid_df[fuel].mean())

    def to_records(self) -> list[dict]:
        """Gibt die Tankstellen als Liste von Dictionaries im API-Format zurück."""
        if self.data.empty:
            return []
        return self.data.to_dict(orient="records")


if __name__ == "__main__":
    # Test-Instanz für die Akzeptanzkriterien
    station_list = StationList.from_csv("data/tankstellen.csv")
    print(f"Erfolgreich geladen: {len(station_list.get_all())} Tankstellen.")
    
    # Tests für die Implementierungen
    print("Durchschnittspreis E10:", station_list.mean_price("e10"))
    cheapest_super = station_list.cheapest("e10")
    print("Günstigste E10 Tankstelle:", cheapest_super)
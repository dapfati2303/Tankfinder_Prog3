"""Hilfsfunktionen für die Tankstellen-Karten-Demo."""

KRAFTSTOFFE = {
    "e5": "Super E5",
    "e10": "Super E10",
    "diesel": "Diesel",
}


def top_tankstellen(tankstellen, kraftstoff, anzahl=5):
    """Gibt Tankstellen mit einem Preis sortiert vom günstigsten zurück."""
    mit_preis = [
        station
        for station in tankstellen
        if station.get(kraftstoff) is not None
    ]
    return sorted(mit_preis, key=lambda station: station[kraftstoff])[:anzahl]


def guenstigste_tankstelle(tankstellen, kraftstoff):
    """Gibt die günstigste Tankstelle zurück oder None, falls kein Preis vorliegt."""
    sortiert = top_tankstellen(tankstellen, kraftstoff, anzahl=1)
    return sortiert[0] if sortiert else None
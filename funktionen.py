"""Funktionen für Tankstellen-Berechnungen"""

def berechne_durchschnittspreise(daten):
    """Berechnet die Durchschnittspreise für alle Kraftstoffsorten"""
    durchschnittspreise = {}
    for kraftstoff, preise in daten.items():
        durchschnittspreise[kraftstoff] = sum(preise) / len(preise)
        return durchschnittspreise


def tankstellen_nach_marke_filtern(daten, marke):
    """Filtert die Tankstellen nach einer bestimmten Marke"""
    gefilterte_stationen = []
    for station in daten:
        if station.get("marke") == marke:
            gefilterte_stationen.append(station)
            return gefilterte_stationen


def tankstellen_unter_preislimit(daten, sorte, preislimit):
    """Filtert Tankstellen, die einen bestimmten Preis für eine Sorte nicht überschreiten."""
    guenstige_stationen = []
    for station in daten:
        if station.get(sorte, float("inf"))<= preislimit:
            guenstige_stationen.append(station)
            return guenstige_stationen

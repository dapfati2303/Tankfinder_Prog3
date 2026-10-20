"""Hilfsfunktionen für die Tankstellen-Daten"""


def nur_offene(daten):
    """Gibt nur die Tankstellen zurück, die gerade offen sind."""
    ergebnis = []
    for tankstelle in daten:
        if tankstelle ["offen"]:
            ergebnis.append(tankstelle)
    return ergebnis          

def durchschnittspreise(daten, sorte):
    """Berechnet den Durchschnittspreis einer Spritsorte."""
    if not daten:
        return None
    preise = []
    for tankstelle in daten:
        preise.append(tankstelle[sorte])
    return sum(preise) / len(preise)
    
def guenstigste(daten, sorte):
    """Gibt die Tankstellen mit dem niedrigsten Preis der Sorte zurück."""
    if not daten:
        return None
    beste = daten[0]
    for tankstelle in daten:
        if tankstelle[sorte] < beste[sorte]:
            beste = tankstelle
    return beste        
















if __name__ == "__main__":
    from daten import TANKSTELLEN

    offene = nur_offene(TANKSTELLEN)
    print(len(offene), "von", len(TANKSTELLEN), "Tankstellen sind offen")

    print(f"Durchschnitt E5: {durchschnittspreise(TANKSTELLEN, 'e5'):.3f}")

    billig = guenstigste(TANKSTELLEN, "e5")
    print(f"Günstigste: {billig['name']} in {billig['ort']} für {billig['e5']:.3f} €")


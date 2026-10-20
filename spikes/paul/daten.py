"""Beispieldaten: Tankstellen im Allgäu und Außerfern."""   


TANKSTELLEN = [
    {"name": "V-Markt", "ort": "Füssen", "lat": 47.569, "lng": 10.671, "e5": 2.099, "offen": True},
    {"name": "JET",     "ort": "Füssen", "lat": 47.569, "lng": 10.688, "e5": 2.109, "offen": True},
    {"name": "Agip Kempten", "ort": "Kempten", "lat": 47.73, "lng": 10.327, "e5": 2.31, "offen": True},
    {"name": "Eni Kempten", "ort": "Kmepten", "lat": 47.56, "lng": 9.34, "e5": 2.234, "offen": False}
]



if __name__ == "__main__":
    print(len(TANKSTELLEN), "Tankstellen")
    for tankstelle in TANKSTELLEN:
        status = "offen" if tankstelle["offen"] else "geschlossen"
        print(f"{tankstelle['name']:<15} {tankstelle['ort']:<10} {tankstelle['e5']:.3f} € {status}")
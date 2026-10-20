"""Beispieldaten: Tankstellen im Allgäu und Außerfern."""   


TANKSTELLEN = [
    {"name": "V-Markt", "ort": "Füssen", "lat": 47.569, "lng": 10.671, "e5": 2.099, "offen": True},
    {"name": "JET",     "ort": "Füssen", "lat": 47.569, "lng": 10.688, "e5": 2.109, "offen": True},
    {"name": "Agip Kempten", "ort": "Kempten", "lat": 47.73, "lng": 10.327, "e5": 2.31, "offen": True},
    {"name": "Eni Friedrichshafen", "ort": "Kmepten", "lat": 47.657, "lng": 9.485, "e5": 2.234, "offen": False},
        {"name": "Aral Kaufbeuren",       "ort": "Kaufbeuren",    "lat": 47.880, "lng": 10.622, "e5": 2.069, "offen": True},
    {"name": "Shell Memmingen",       "ort": "Memmingen",     "lat": 47.984, "lng": 10.181, "e5": 2.119, "offen": True},
    {"name": "Esso Sonthofen",        "ort": "Sonthofen",     "lat": 47.515, "lng": 10.282, "e5": 2.089, "offen": False},
    {"name": "Avia Pfronten",         "ort": "Pfronten",      "lat": 47.582, "lng": 10.554, "e5": 2.059, "offen": True},
    {"name": "BayWa Marktoberdorf",   "ort": "Marktoberdorf", "lat": 47.778, "lng": 10.617, "e5": 2.039, "offen": True},
    {"name": "OMV Immenstadt",        "ort": "Immenstadt",    "lat": 47.560, "lng": 10.220, "e5": 2.099, "offen": True},
    {"name": "Total Oberstdorf",      "ort": "Oberstdorf",    "lat": 47.410, "lng": 10.279, "e5": 2.149, "offen": False}
]



if __name__ == "__main__":
    print(len(TANKSTELLEN), "Tankstellen")
    for tankstelle in TANKSTELLEN:
        status = "offen" if tankstelle["offen"] else "geschlossen"
        print(f"{tankstelle['name']:<15} {tankstelle['ort']:<10} {tankstelle['e5']:.3f} € {status}")
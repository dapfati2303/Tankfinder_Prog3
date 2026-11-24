# Tankfinder

> **Aktuelles Sprintziel (Sprint 3, 19.11.–02.12.2026):**
> Die Karte zeigt echte Spritpreise von Tankerkönig rund um den Standort des Nutzers.
> Das Request-Limit wird eingehalten, und Testdaten bleiben als Fallback nutzbar.

Tankfinder ist eine Web-App, die Autofahrern die günstigsten Tankstellen (Super E5, Super E10, Diesel)
in ihrer Umgebung zeigt: auf einer Karte und als sortierte Liste, mit Filtern und später mit Route zur Tankstelle.

Projekt im Modul E 308 Programmieren 3, Hochschule Kempten, Wintersemester 2026/27.

## Funktionen

| Funktion | Stand |
|---|---|
| Tankstellen auf Karte und in Tabelle anzeigen | ✅ Sprint 2 |
| Filter: Spritsorte, Höchstpreis, nur geöffnete | ✅ Sprint 2 |
| Sortierung nach Preis, günstigste zuerst | ✅ Sprint 2 |
| Echte Preise von Tankerkönig rund um den Standort | 🔄 Sprint 3 |
| Standort per Browser, Suchradius bis 25 km | 🔄 Sprint 3 |
| Route zur gewählten Tankstelle | ⏳ geplant |

## Technik und warum

| Teil | Wahl | Begründung |
|---|---|---|
| Backend | **Flask** (Python) | Schlankes Web-Framework: liefert die Webseite aus und stellt eine JSON-Schnittstelle (`/api/stations`) bereit. Backend und Oberfläche sind dadurch klar getrennt und können parallel entwickelt werden. |
| Karte | **Leaflet** (JavaScript) mit OpenStreetMap | Kostenlos, ohne API-Key, sehr verbreitet. Marker, Popups und Standort per Browser sind direkt möglich, ohne dass bei jeder Änderung die ganze Seite neu lädt. |
| Datenverarbeitung | **pandas** | Filtern und Sortieren von Tabellen mit wenig Code, gekapselt in der Klasse `StationList`. |
| Daten | **Tankerkönig-API** + CSV-Testdaten | Tankerkönig liefert echte Preise der Markttransparenzstelle. Die CSV dient für Tests und als Fallback (die API erlaubt nur 1 Anfrage pro Minute). |

**Warum nicht Streamlit?** Streamlit haben wir in Sprint 1 im Spike ausprobiert. Für eine interaktive Karte mit eigener Logik
im Browser (Standort, Marker aktualisieren ohne Neuladen) ist die Kombination Flask + Leaflet flexibler.

## Installation und Start

Voraussetzungen: Python 3.10 oder neuer, Git.

```bash
git clone https://github.com/dapfati2303/Tankfinder_Prog3.git
cd Tankfinder_Prog3

python -m venv .venv
source .venv/Scripts/activate      # Windows (Git Bash)
# source .venv/bin/activate        # macOS/Linux

pip install -r requirements.txt
python app.py
```

Dann im Browser öffnen: http://127.0.0.1:5000. Beenden mit `Strg + C`.

### Tankerkönig-API-Key (optional)

Ohne Key läuft die App mit den Testdaten aus `data/tankstellen.csv`.
Für echte Preise:

1. Key kostenlos beantragen: https://creativecommons.tankerkoenig.de
2. `.env.example` nach `.env` kopieren und den Key eintragen.
3. Die `.env` wird **nie** committet (steht in `.gitignore`).

## Projektstruktur

```
app.py                  Einstiegspunkt: Flask-App und Routen
tankfinder/
  application.py        Application-Klasse (Name, Version, Team)
  stations.py           StationList: Filtern, Sortieren, Auswerten
  tankerkoenig.py       Zugriff auf die Tankerkönig-API
frontend/index.html     Oberfläche mit Leaflet-Karte
data/tankstellen.csv    Testdaten (10 Tankstellen im Allgäu)
docs/api.md             Schnittstelle zwischen Backend und Frontend
docs/sprints/           Planning, Review und Retro je Sprint
spikes/                 Experimente aus Sprint 1
```

## Architektur

Folgt in Sprint 4: Klassendiagramm, welche OOP-Konzepte wo eingesetzt werden und wo bewusst nicht.

## Team

| Name | GitHub |
|---|---|
| Paul Thurner (Product Owner) | pthurner0815 |
| Adrian Pfatischer | … |
| Julian Fischer | … |
| Raphael Goester | … |

Die Rollen je Sprint (inkl. Scrum Master) stehen in `docs/sprints/`.

## Arbeitsweise

- Scrum mit 2-Wochen-Sprints, Board in GitHub Projects
- Änderungen nur über Pull Requests mit Review, verknüpft mit `Closes #N`
- KI-unterstützter Code wird im Pull Request gekennzeichnet

## Datenquellen und Lizenzen

- Spritpreise: [Tankerkönig](https://creativecommons.tankerkoenig.de), Lizenz CC BY 4.0
- Karte: © [OpenStreetMap](https://www.openstreetmap.org/copyright)-Mitwirkende

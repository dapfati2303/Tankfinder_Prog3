# API: Tankstellen

## `GET /api/stations` 

Liefert Tankstellen aus der aktuellen Datenquelle. Die Datenquelle wird in `env` gewählt:
`DATENQUELLE=csv` (Testdaten aus `data/tankstellen.csv`) oder `DATENQUELLE=api` (Tankerkönig).


### Parameter

| Parameter   | Typ        | Pflicht | Standard | Beschreibung                            |
|-------------|------------|---------|----------|-----------------------------------------|
| `fuel`      | Text       | nein    | `e5`     | Spritsorte: `e5`, `e10` oder `diesel`   |
| `open_only` | true/false | nein    | `false`  | nur geöffnete Tankstellen               |
| `max_price` | Zahl       | nein    | -        | nur Tankstellen bis zu diesem Preis (€) |
| `lat`       | Zahl       | nein*   | -        | Breitengrad des Standorts (-90 bis 90)  |
| `lng`       | Zahl       | nein*   | -        | Längengrad des Standorts (-180 bis 180) |
| `radius`    | Zahl       | nein    | `10`     | Suchradius in km (1 bis 25)             |

\* `lat` und `lng` immer zusammen angeben. Ohne Standort verhält sich die API wie in Sprint 2.

Regeln:
- Sortierung immer nach Preis der gewählten Sorte, günstigste zuerst.
- Tankstellen ohne Preis für die gewählte Sorte werden nicht geliefert.
- `radius` gilt nur zusammen mit `lat`/`lng`.

Bsp. ohne Standort: `/api/stations?fuel=e5&open_only=true&max_price=1.87`
Bsp. mit Standort: `/api/stations?fuel=diesel&lat=47.7267&lng=10.3139&radius=10`


### Antwort (Status 200)

Sortiert nach Preis der gewählten Sorte, günstigste zuerst.

```json
{
    "fuel": "e5",
    "count": 2,
    "stations": [
        {
            "id": 8,
            "name": "BayWa Marktoberdorf",
            "brand": "BayWa",
            "street": "Kemptener Str. 40",
            "city": "Marktoberdorf",
            "lat": 47.778,
            "lng": 10.617,
            "e5": 1.859,
            "e10": 1.799,
            "diesel": 1.729,
            "is_open": true,
            "dist": null 
        },
        {
            "id": 7,
            "name": "Avia Pfronten",
            "brand": "Avia",
            "street": "Tiroler Str. 8",
            "city": "Pfronten",
            "lat": 47.582,
            "lng": 10.554,
            "e5": 1.869,
            "e10": 1.809,
            "diesel": 1.739,
            "is_open": true,
            "dist": null
        }
    ]
}
```

Keine Treffer: `"count": 0` und `"stations": []` (kein Fehler).
`dist` = Entferung zum Standort in km (eine Nachkommastelle), `null` wenn kein Standort angegebn ist.

### Fehler (Status 400)

Ungültige Eingabe, z.b. unbekannte Sorte, nur `lat` ohne `lng`, Koordinaten außerhalb des Bereichs, `radius` nicht zwischen 1 und 25.

```json
{ "error": "Unbekannte Spritsorte: lpg" }
```

```json
{ "error": "radius muss zwischen 1 und 25 liegen" }
```

### Fehler (Status 429)

Nur bei `DATENQUELLE=api`: Tankerkönig erlaubt höchstens 1 Anfrage pro Minute.
`retry_after` = Sekunden bis zur nächsten erlaubten Anfrage.

```json
{ "error": "Zu viele Anfragen, bitte kurz warten", "retry_after": 42 }
```

## `GET /api/info`

```json
{ "status": "Tankfinder 0.2.0: Günstigste Tankstellen im Umkreis finden und Route anzeigen..." }
```

## Testwerte (`data/tankstellen.csv`)

Gelten für `Datenquelle=csv`ohne Standort (`lat`/`lng` weglassen).

| Abfrage                          | Erwartung                                      |
|----------------------------------|------------------------------------------------|
| alle Tankstellen                 | 10                                             |
| nur geöffnete                    | 8 (geschlossen: Esso Sonthofen, Total Oberstdorf) |
| Durchschnitt E5                  | 1,914 €                                        |
| Durchschnitt E5, nur geöffnete   | 1,904 €                                        |
| günstigste E5                    | BayWa Marktoberdorf, 1,859 €                   |
| E5 bis 1,90 €                    | 4 (V-Markt, Agip, Avia, BayWa)                 |
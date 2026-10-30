# API: Tankstellen

## `GET /api/stations` 

Liefert Tankstellen aus der aktuellen Datenquelle (Sprint 2: `data/tankstellen.csv`).

### Paramter

| Parameter   | Typ        | Pflicht | Standard | Beschreibung                            |
|-------------|------------|---------|----------|-----------------------------------------|
| `fuel`      | Text       | nein    | `e5`     | Spritsorte: `e5`, `e10` oder `diesel`   |
| `open_only` | true/false | nein    | `false`  | nur geöffnete Tankstellen               |
| `max_price` | Zahl       | nein    | –        | nur Tankstellen bis zu diesem Preis (€) |

Bsp.: `/api/stations?fuel=e5&open_only=true&max_price=1.87`

### Antwort (Status200)

Sortiert nach Preis der gewählten Sorte, günstigste zuerst.

```json
{
    "fuel": "e5",
    "count": 2,
    "stations": [
        {
            "id": 8,
            "name": "BAyWa Marktoberdorf",
            "brand": "BayWa",
            "street": "Kemptener Str. 40",
            "city": "Marktoberdorf",
            "lat": 47.778,
            "lng": 10.617,
            "e5": 1.858,
            "e10": 1.799"
            "diesel": 1.799,
            "is_open": true
        },
        {
            "id". 7,
            "name": "Avia Pfronten",
            "brand": "Avia",
            "street": "Tiroler Str. 8",
            "coity": "Pfronten",
            "lat": 47.582,
            "lng": 10.554,
            "e5": 1.869,
            "e10": 1.809,
            "diesel": 1.739,
            "is_open": true
        }
    ]
}
```

Keine Treffer: `"count": 0` und `"stations": []` (kein Fehler).

### Fehler (Status 400)

```json
{ "error": "Unbekannte Spritsorte: lpg" }
```

## `GET /api/info`

```json
{ "status": Tankfinder 0.1.0: Günstigste Tankstellen im Umkreis funden und Route anzeigen..." }
```

## Testwerte (`data/tankstellen.csv`)

| Abfrage                          | Erwartung                                      |
|----------------------------------|------------------------------------------------|
| alle Tankstellen                 | 10                                             |
| nur geöffnete                    | 8 (geschlossen: Esso Sonthofen, Total Oberstdorf) |
| Durchschnitt E5                  | 1,914 €                                        |
| Durchschnitt E5, nur geöffnete   | 1,904 €                                        |
| günstigste E5                    | BayWa Marktoberdorf, 1,859 €                   |
| E5 bis 1,90 €                    | 4 (V-Markt, Agip, Avia, BayWa)                 |
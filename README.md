# Vorbereitung
- Python >=3.8.7 installieren (https://it-services.muenchen.de/sp?id=sc_cat_item&sys_id=67f8144b1b252154a70c433c8b4bcb4d&table=sc_cat_item)
- `uv` einrichten: https://git.muenchen.de/kicc/kicc/-/wikis/Client-Entwicklung/uv#installation-von-uv
- Package-Management einrichten: https://git.muenchen.de/kicc/kicc/-/wikis/Client-Entwicklung/uv#artifactory-als-paket-quelle-angeben

# Funktion
Alle `.json`-Dateien aus einem Ordner werden einzeln in CSV-Dateien umgewandelt. Die CSV-Dateien werden gleich benannt, wie die JSON-Dateien.
1. Alle `.json`-Dateien werden eine nach dem anderen aus dem gegebenen Ordner ausgelesen.
2. Die JSON-Datei wird umstrukturiert und für die CSV-Umwandlung vorbereitet.
3. Die Daten werden in eine CSV-Datei geschrieben unter `output/<filename>.csv`. Als **Trennzeichen** wird `;` benutzt.
4. Der Ordner `output` befindet sich im gleichen Ordner wie die Python-Datein `converter.py` und beinhaltet alle CSV-Dateien.

> Gleichnamige CSV-Dateien werden überschrieben!!

Die Funktion nimmt 2 mögliche Parameter an:
- `<merge_csv?>` Sollen alle Daten in eine CSV zusammengeführt werden? `True` oder `False` (Standardmäßig `False`)
- `<folder>` Ordner mit den JSON Dateien. (Standardmäßig `data`)

Die Reihenfolge der Parameter beim AUfruf ist wichtug!! Daraus ergeben sich folgende Aufrufmöglichkeiten:
```
python converter.py
```
```
python converter.py <merge_csv?>
```
```
python converter.py <merge_csv?> <folder>
```

# Benutzung
1. Im Terminal in den Ordner wechseln in dem sich die Python-Datein `converter.py` befindet.

2. Im Terminal ausführen mit:
```
python converter.py <merge_csv?> <folder>
```
Wichtig dabei ist nur, dass der Ordner sich an der gleichen Stelle befindet wie die Python-Datei. Tiefere Struktur ist auch möglich, wie:
```
python converter.py <merge_csv?> <folder1/folder2>
```

3. Alternativ kann man den Ordner `<folder>` weglassen:
```
python converter.py <merge_csv?>
```
Dabei  wird als der Ordner mit den `.json`-Dateien der Ordner `data` genommen, der sich an der gleichen Stelle befinden muss wie die ausgeführte Python-Datei.

4. Falls `<merge_csv?>` als `True` gesetzt wurde, wird am Ende nur eine CSV `output/all_merged.csv` mit allen Daten erstellt.

# Ordnerstruktur

```
-|
 |-converter.py
 |-README.md
 |-pyproject.toml
 |-uv.lock
 |-.python-version
 |-.gitignore
 |-data/<folder>-|-<JSON Datei>
                 |-<JSON-Datei>
                 |-...
 |-output-|-<CSV Datei>
          |-<CSV Datei>
          |-...
 |-.venv-|-...

```
# konverter-norgeskart-projeksjon

Dette scriptet konverterer norgeskart (kommunegrenser og fylkegrenser) fra genorge i UTM-33 projeksjon 
til EPSG:3857 som Google og Leaflet bruker.
Scriptet bruker python biblioteket [pyproj](https://pypi.org/project/pyproj/) for å projeksjon konverteringen.

Norges offisielle kart database, geonorge, gir bare ut grensekoordinatene i UTM 33 projeksjon, 
som ikke fungerer med populære javascript kart verktøy som f.eks. Leaflet. 
Dette scriptet konverterer koordinatene til projeksjonen som Leaflet og Google bruker, kalt EPSG:3857.

De opprinnelige grensedata fra Geonorge består av veldig mange koordinater som medfører stor filstørrelse. 
Du kan redusere antall koordinater ved å bruke [mapshaper.org](http://mapshaper.org) til å glatte ut grensene. 
Grensene er blir dermed ikke helt riktige, men reduserer filstørrelsen betraktelig og ser riktig ut på høyt nivå.


## Bruk

1. Last ned offisielle gjeldende kart fra geonorge for [kommuner](https://kartkatalog.geonorge.no/metadata/041f1e6e-bdbc-4091-b48f-8a5990f3cc5b) og [fylker](https://kartkatalog.geonorge.no/metadata/6093c8a8-fa80-11e6-bc64-92361f002671). Husk å velge hele landet, UTM-33 projeksjon og GeoJSON format. Legg disse filene i samme mappe som convert.py scriptet.

2. Installer pakkene som trengs, f.eks. i et virtual environment:
```bash
virtualenv -ppython venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Kjør så scriptet:
```bash
python convert.py
```

4. Etter du har gjort dette kan du bruke [mapshaper.org](http://mapshaper.org) til å redusere antall koordinater og dermed filstørrelsen så det blir litt mer web-vennlig.

5. Enjoy!

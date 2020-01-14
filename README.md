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

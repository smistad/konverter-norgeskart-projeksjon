import pyproj
import json
import numpy
from math import ceil

input_file = 'kommuner-utm33.geojson'
output_file = 'kommuner.json'
name = 'administrative_enheter.fylke'
name = 'administrative_enheter.kommune'

coordinates_per_object = 2000
keep_all = True

#defineprojections
source = pyproj.Proj(proj='utm', zone=33, ellps='WGS84')
target = pyproj.Proj(init='epsg:3857')

#load in data
with open(input_file, 'r') as f:
    data = json.load(f)

data[name]['crs']['properties']['name'] = 'EPSG:3857'
#traverse data in json string
for feature in data[name]['features']:
     #print feature['geometry']['type']
     #print feature['geometry']['coordinates']

    #all coordinates
    coords = feature['geometry']['coordinates']

    #coordList is for each individual polygon
    newCoordLists = []
    for coordList in coords:
        print(len(coordList))
        step = int(ceil(len(coordList)/coordinates_per_object))
        newCoordList = []
        #each point
        counter = 0
        for coordPair in coordList:
            if keep_all or counter % step == 0 or counter + 1 == len(coordList):
                x1 = coordPair[0]
                y1 = coordPair[1]
                #do transformation
                x, y = pyproj.transform(source,target,x1, y1)
                #print(coordPair[0], coordPair[1])
                x, y = source(x1, y1, inverse=True)
                #print(x, y)
                newCoordList.append([x, y])
            counter += 1

        newCoordLists.append(newCoordList)
    feature['geometry']['coordinates'] = newCoordLists

with open(output_file, 'w') as f:
    f.write(json.dumps(data[name]))

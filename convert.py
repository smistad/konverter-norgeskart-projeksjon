import pyproj
import json
import numpy as np
from math import ceil
import sys

if __name__ == "__main__":

    arguments = sys.argv
    if len(arguments) < 3:
        print('Usage: convert.py input-filename.json output-filename.json')
        exit()

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    coordinates_per_object = 2000
    keep_all = True

    #defineprojections
    source = pyproj.Proj(proj='utm', zone=33, ellps='WGS84')
    target = pyproj.Proj(init='epsg:3857')

    #load in data
    with open(input_file, 'r') as f:
        data = json.load(f)

    if 'Fylke' in data:
        name = 'Fylke'
    else:
        name = 'Kommune'

    data[name]['crs']['properties']['name'] = 'EPSG:3857'
    #traverse data in json string
    for feature in data[name]['features']:
         #print feature['geometry']['type']
         #print feature['geometry']['coordinates']

        #all coordinates
        coords = feature['geometry']['coordinates']

        #coordList is for each individual polygon
        regions = []
        for region in coords:
            newCoordLists = []
            for coordList in region:
                print(len(coordList))
                step = int(ceil(len(coordList)/coordinates_per_object))
                newCoordList = []

                array = np.array(coordList)
                newX, newY = source(array[:,0], array[:,1], inverse=True)
                newCoordList = np.column_stack((newX, newY))
                #print(newCoordList.shape)
                newCoordList = newCoordList.tolist()

                newCoordLists.append(newCoordList)
            regions.append(newCoordLists)
        feature['geometry']['coordinates'] = regions

    with open(output_file, 'w') as f:
        f.write(json.dumps(data[name]))

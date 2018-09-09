import requests
import json
import googlemaps
import math
from flask import Flask

key = 'AIzaSyBEEc2mt53Pmde3PSeIQ0umg0PXt8AQbxQ';
gmaps = googlemaps.Client(key='AIzaSyBEEc2mt53Pmde3PSeIQ0umg0PXt8AQbxQ')
equatorialDegreeLength = 69.172;

testJson = {};
testJson['latitude'] = "40.5974714";
testJson['longitude'] = "-73.951458";

#app = Flask(__name__);

#@app.route('/latlong/<latlong>')
#def api_latlong(latlong):

def main(coords):
    location = {};
    location['latitude'] = coords['latitude'];
    location['longitude'] = coords['longitude'];
    location['elevation'] = elevation(coords);
    #the second 
    g = createGrid(location, 0.4, 9);
    print("the highest point is:")
    high = findhighest(g, location);
    print(high);

def createGrid(location, size, resolution):
    latitude = l(float(location["latitude"]));
    longitude = l(float(location["longitude"]));
    pointarr = [];
    for r in range(-(resolution // 2), resolution // 2 + 1):
        points = [];
        latratio = (r / (resolution // 2));
        for c in range(-(resolution // 2), resolution // 2 + 1):
            lonratio = (c / (resolution // 2));
            newlat = round(float(location["latitude"]) + (size * latratio * (1 / latitude)), 4)
            newlon = round(float(location["longitude"]) + (size * lonratio * (1 / longitude)), 4)
            locObj = {};
            locObj["latitude"] = newlat;
            locObj["longitude"] = newlon;
            locObj["elevation"] = elevation(locObj);
            points.append(locObj)
        pointarr.append(points);
    return pointarr;

def findhighest(grid, location):
    highest = location;

    for row in grid:
        for loc in row:
            if float(loc['elevation']) > float(highest['elevation']):
                highest = loc;
    return highest;


def elevation(coords):
    coordString = str(coords['latitude']) + "," + str(coords['longitude']);
    payload = {"locations": coordString, "key": key};

    return(requests.get('https://maps.googleapis.com/maps/api/elevation/json', params = payload).json()['results'][0]['elevation']);

def elevations(coords):
    coordstring = "";
    for str in coords:
        coordstring += (str + "|");
    coordstring = coordstring[:1];
    return elevation(coordstring);

def l(lt):
    rlt = math.radians(lt);
    return math.cos(rlt) * equatorialDegreeLength;

main(testJson);
#elevation(testJson);
#if __name__ == "__main__":
    #app.run();


import os
import dotenv
import requests
import config
import pandas as pd

def getLocationfor(item):
    lat = item['latitude']
    lon = item['longitude']
    loc = {
            'type':'Point',
            'coordinates':[float(lon), float(lat)]
        }
    return loc

def deduplicate(listDict):
    df1 = pd.DataFrame(listDict)
    df2 = df1.drop_duplicates()
    return df2.to_dict(orient='records')


def getPlacebyQuery(lat, lon, query, radius):
    url = 'https://api.foursquare.com/v2/venues/explore'
    params = dict(
      client_id=os.getenv('F_CLIENT_ID'),
      client_secret=os.getenv('F_CLIENT_SECRET'),
      v='20180323',
      ll=f"{lat},{lon}",
      radius = radius,
      query=query,
      #limit=10
    )
    res = requests.get(url, params=params)
    return res.json()['response']['groups'][0]['items']

def getPlacebyCategory(lat, lon, categoryId, radius):
    url = 'https://api.foursquare.com/v2/venues/explore'
    params = dict(
      client_id=os.getenv('F_CLIENT_ID'),
      client_secret=os.getenv('F_CLIENT_SECRET'),
      v='20180323',
      ll=f"{lat},{lon}",
      radius = radius,
      categoryId=categoryId,
      #limit=10
    )
    res = requests.get(url, params=params)
    return res.json()['response']['groups'][0]['items']

def getNearbyPlacesCat(coll, categoryId, category, radius):
    places = []
    places_dict = {}
    categoryId = categoryId
    radius = radius
    for company in coll:
        lon = str(company['offices']['longitude'])
        lat = str(company['offices']['latitude'])
        try:
            foursquare = getPlacebyCategory(lat, lon, categoryId, radius)
            for place in foursquare:
                lat = place['venue']['location']['lat']
                lon = place['venue']['location']['lng']
                places_dict['name'] = place['venue']['name']
                places_dict['category'] = category
                places_dict['latitude'] = place['venue']['location']['lat']
                places_dict['longitude'] = place['venue']['location']['lng']
        except:
            places_dict = {}
        if len(places_dict) > 0:
            places.append(places_dict)
        places_dict = {}
    return deduplicate(places)

def getNearbyPlacesQuery(coll, query, category, radius):
    places = []
    places_dict = {}
    query = query
    radius = radius
    for company in coll:
        lon = str(company['offices']['longitude'])
        lat = str(company['offices']['latitude'])
        try:
            foursquare = getPlacebyQuery(lat, lon, query, radius)
            for place in foursquare:
                lat = place['venue']['location']['lat']
                lon = place['venue']['location']['lng']
                places_dict['name'] = place['venue']['name']
                places_dict['category'] = category
                places_dict['latitude'] = place['venue']['location']['lat']
                places_dict['longitude'] = place['venue']['location']['lng']
        except:
            places_dict = {}
        if len(places_dict) > 0:
            places.append(places_dict)
        places_dict = {}
    return deduplicate(places)

def giveScore(values):
    if all(value>0 for value in values):
        return 1
    else:
        return 0

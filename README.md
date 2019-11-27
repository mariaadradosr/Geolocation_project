# Geolocation Project

This project is meant to help a company in the task of deciding where its office is to be set up given different preferences from its team: 
- Nearby daycare since 30% of the company have at least one child.
- Nearby Starbucks.
- Nearby airport since account managers travel a lot.
- Nearby some place to go to party since all people in the company have between 24 and 40 years old.
- Nearby vegan restaurant since the CEO is vegan.

## Background

I have **mongodb crunchbase database** as starting point, which is a database that contains information about worldwide innovative companies (https://www.crunchbase.com/). 
In order to find the nearby places I use **Foursquare API** (https://developer.foursquare.com/).
I use **Google's Geocoding API** as well to convert addresses into latitude and longitude geographic coordinates.

## Directories and Files

- `src` contains the jupyter notebook where I develop the project  (`Project.ipynb`) and several python files that include the different functions used throughout the project.
- `input` contains source files for some of the functions as well as the initial dataset.

## Getting Started

You just need to go through the Jupyter Notebook file where I will guide you throughout the process I've followed to find the perfect location for the company.

## Prerequisites

You will need to install the following modules:

    folium==0.10.0
    googlemaps==3.1.4
    numpy==1.17.3
    pandas==0.25.2
    pymongo==3.9.0
    requests==2.22.0


Hope you enjoy it! :) 









# ----------------------------------------------------------------------- #

# CoronaTracker

# File:         DataProcessing.py
# Maintainer:   DP Team
# Last Updated: 2020-04-13
# Language:     Python 3.7

# ------------------------------------------------------------------------ #

# ------------------------------------------------------------------------ #
# Initialization
# ------------------------------------------------------------------------ #

# Path
# ---------------------------------------------#
import os, sys
app_root = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))  

# Load external dependencies
# ---------------------------------------------#
## General Dependencies
import pandas as pd
import numpy as np

## Geocoding Dependencies
import geopy
from geopy.geocoders import Nominatim

# ------------------------------------------------------------------------ #
# Define Functions
# ------------------------------------------------------------------------ #

# location_corona_data
# ---------------------------------------------#
def location_mobility_data(longitude=None, latitude=None ,
	datapath = os.path.join(app_root, "Backend/Data/CoronaData.csv")):

	# Load the data
	mobility_df = pd.read_csv(datapath, encoding="utf-8")

	# Geocode the longitude/latitude data if not provided with country

	## Initialize the geocoder
	locator      = Nominatim(user_agent="myGeocoder")

	## Obtain the country
	coordinates  = str(latitude) + ", " + str(longitude)
	geocode_data = locator.reverse(coordinates)
	country      = geocode_data.raw['address']['country']

	#####
	# Subset to the location
	mobility_location_df = mobility_df[mobility_df["region"]==country]

	# Generate location-specific statistics
	driving = mobility_location_df[mobility_location_df["transportation_type"] == "driving"]
	walking = mobility_location_df[mobility_location_df["transportation_type"] == "walking"]

	walking_chg = 1 - walking.iloc[0,-1]/walking.iloc[0,3]
	walking_chg = (walking_chg*100).round(decimals = 1)

	driving_chg = 1 - driving.iloc[0,-1]/driving.iloc[0,3]
	driving_chg = (driving_chg*100).round(decimals = 1)

	# Return the summary statistics
	return([country, walking_chg, driving_chg])

# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #


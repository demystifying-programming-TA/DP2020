# ----------------------------------------------------------------------- #

# MobilityTracker

# File:         dataprocessing.py
# Maintainer:   DP Team
# Last Updated: 2020-04-13
# Language:     Python 3.7

# ------------------------------------------------------------------------ #

# ------------------------------------------------------------------------ #
# Initialization
# ------------------------------------------------------------------------ #

# Load dependencies
# ---------------------------------------------#
import pandas as pd

# ------------------------------------------------------------------------ #
# Define Functions
# ------------------------------------------------------------------------ #

# location_mobility_data
# ----------------------------
def location_mobility_data(longitude, latitude):

	# Load the data
	mobility_df = pd.read_csv("backend/data/CoronaData.csv", 
		encoding="utf-8")

	# Reverse geocode (longitude, latitude > country)
	country = "United States"

	# Extract data for country

	# Extract data for walking & calculate change in # of walking calls
	walking_chg = 20
	
	# Extract data for driving & calculate change in # of driving calls
	driving_chg = 30
	
	# Return the results
	return([country, walking_chg, driving_chg])

# ------------------------------------------------------------------------ #
# Analyze
# ------------------------------------------------------------------------ #

## Try the location_mobility_data() function
## Note: Longitude,latitude refer to the United States
print(location_mobility_data(longitude = -71.08328259999999 , latitude = 42.3662154))

# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #


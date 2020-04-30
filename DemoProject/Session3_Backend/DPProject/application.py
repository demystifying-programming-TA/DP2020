# ----------------------------------------------------------------------- #

# CoronaTracker

# File:         application.py
# Maintainer:   DP Team
# Last Updated: 2020-04-13
# Language:     Python 3.7

# ------------------------------------------------------------------------ #

# ------------------------------------------------------------------------ #
# Initialization
# ------------------------------------------------------------------------ #

# Load internal dependencies
# ---------------------------------------------#
import os, sys
sys.path.append('Backend')
from DataProcessing import *

# ------------------------------------------------------------------------ #
# Test Functions
# ------------------------------------------------------------------------ #

# update_owncountry
# ---------------------------------------------#

## Note: Try with US, Germany, UK
for i in [[-71.08328259999999, 42.3662154],[10.48328259999999, 51.3662154],[-1.78328259999999, 52.4662154]]:
	try:
		long = i[0]
		lat  = i[1]
		data = location_mobility_data(longitude = long, latitude = lat)
		print("Country name: ", data[0])
		print("% decrease in walking: ",data[1])
		print("% decrease in driving ",data[2])
		
	except:
		print("Country not found.")

# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #

# ----------------------------------------------------------------------- #

# MobilityTracker

# File:         application.py
# Maintainer:   DP Team
# Last Updated: 2020-04-13
# Language:     Python 3.7

# ------------------------------------------------------------------------ #

# ------------------------------------------------------------------------ #
# Initialization
# ------------------------------------------------------------------------ #

# Load dependencies
# ---------------------------------------------#
import sys
sys.path.append('Backend')
import dataprocessing as dp

# ------------------------------------------------------------------------ #
# Test Functions
# ------------------------------------------------------------------------ #

## Note: Try with US, Germany, UK
for i in [[-71.08328259999999, 42.3662154],[10.48328259999999, 51.3662154],[-1.78328259999999, 52.4662154]]:
	try:
		long = i[0]
		lat  = i[1]
		data = dp.location_mobility_data(longitude = long, latitude = lat)
		print("Country name: ", data[0])
		print("Decrease in # of walking calls (%): " + str(data[1]))
		print("Decrease in # of driving calls (%):" + str(data[2]))
		
	except:
		print("Country not found.")

# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #

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

## Try the location_mobility_data() function
## Note: Longitude,latitude refer to the United States
data = dp.location_mobility_data(longitude = -71.08328259999999, 
	latitude = 42.3662154)
print("Country name: ", data[0])
print("Decrease in # of walking calls (%): " + str(data[1]))
print("Decrease in # of driving calls (%):" + str(data[2]))

# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #

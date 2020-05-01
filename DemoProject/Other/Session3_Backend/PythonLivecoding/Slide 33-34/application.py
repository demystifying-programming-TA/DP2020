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
print(dp.location_mobility_data(longitude = -71.08328259999999 , latitude = 42.3662154))

# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #
#
# (c) Tribecamp 2020
# Authored by:
# Kees van Voorthuizen <kees.van.voorthuizen@gmail.com>
#

import sys
import yaml

filename = sys.argv[1]

# Load the config
file = open(filename, "r")
config = yaml.load(file,Loader=yaml.FullLoader)

# TODO: remove
print(config)

# Clean up
file.close()

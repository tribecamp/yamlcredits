#
# (c) Tribecamp 2020
# Authored by:
# Kees van Voorthuizen <kees.van.voorthuizen@gmail.com>
# License: MIT
#

import sys
import yaml
from format import formatCredits, formatSubtitle

def generateOutput(config):
  """
  Generates the final output.
  """
  return "\n".join([
    "# Credits",
    formatSubtitle(config["subtitle"]),
    "",
    formatCredits(config["credits"])
  ]).strip()

def main():
  """
  Entrypoint.
  """
  # The filename
  filename = sys.argv[1]

  # Load the config
  file = open(filename, "r")
  config = yaml.load(file, Loader=yaml.FullLoader)

  output = generateOutput(config)

  # Print the output to stdout
  print(output)

  # Clean up
  file.close()

if __name__ == '__main__':
  main()

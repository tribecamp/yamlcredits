#
# (c) Tribecamp 2020
# Authored by:
# Kees van Voorthuizen <kees.van.voorthuizen@gmail.com>
#

import sys
import yaml

def formatContribution(contribution):
  """
  Formats a contribution.
  """
  return "  - {0}\n".format(contribution)

def formatCredits(entry):
  """
  Formats an entry in the list of credits.
  """
  return "\n".join([
    "- **{0}**".format(entry["name"]),
    "".join(map(formatContribution, entry["contributions"]))
  ])

def generateOutput(config):
  """
  Generates the final output.
  """
  return "\n".join([
    "# Credits",
    config["subtitle"].strip(),
    "",
    "".join(map(formatCredits, config["credits"]))
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

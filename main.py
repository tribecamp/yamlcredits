#
# (c) Tribecamp 2020
# Authored by:
# Kees van Voorthuizen <kees.van.voorthuizen@gmail.com>
#

import sys
import yaml

def formatCredits(entry):
  """
  Parses an entry from the credits array.
  """
  contributions = entry["contributions"]

  return """
- **{name}**
{contributions}
  """.format(
    name=entry["name"],
    contributions=''.join(map(lambda c: "  - " + c + "\n", contributions))
  ).strip()

filename = sys.argv[1]

# Load the config
file = open(filename, "r")
config = yaml.load(file, Loader=yaml.FullLoader)

output = """

# Credits
{subtitle}

{credits}

""".format(
  subtitle=config["subtitle"].strip(),
  credits='\n'.join(map(formatCredits, config["credits"]))
).strip()

print(output)

# Clean up
file.close()

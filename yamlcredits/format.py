#
# (c) Tribecamp 2020
# Authored by:
# Kees van Voorthuizen <kees.van.voorthuizen@gmail.com>
#

def formatContribution(contribution):
  """
  Formats a contribution.
  """
  return "  - {0}\n".format(contribution)

def formatCreditsEntry(entry):
  """
  Formats an entry in the list of credits.
  """
  return "\n".join([
    "- **{0}**".format(entry["name"]),
    "".join(map(formatContribution, entry["contributions"]))
  ])

def formatCredits(credits):
  """
  Formats a list of credits.
  """
  return "".join(
    map(formatCreditsEntry, credits)
  )

def formatSubtitle(subtitle):
  """
  Formats a subtitle.
  """
  return subtitle.strip()

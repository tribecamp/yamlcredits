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

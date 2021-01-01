#
# (c) Tribecamp 2020
# Authored by:
# Kees van Voorthuizen <kees.van.voorthuizen@gmail.com>
# License: MIT
#

from socials import github, linkedin

def formatContribution(contribution):
  """
  Formats a contribution.
  """
  return "  - {0}\n".format(contribution)

def formatSocials(socials):
  """
  Formats socials.
  """
  social_links = []
  if "github" in socials:
    social_links.append(github(socials["github"]))
  if "linkedin" in socials:
    social_links.append(linkedin(socials["linkedin"]))
  return " ".join(social_links)

def formatCreditsEntry(entry):
  """
  Formats an entry in the list of credits.
  """
  return "\n".join([
    "- **{0}** {1}".format(
      entry["name"],
      formatSocials(entry["socials"])
    ),
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

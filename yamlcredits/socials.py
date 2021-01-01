#
# (c) Tribecamp 2020
# Authored by:
# Kees van Voorthuizen <kees.van.voorthuizen@gmail.com>
# License: MIT
#

def getImageLink(raw_link, caption):
  """
  Converts a raw link to a Markdown image link.
  """
  return "[{caption}]({link})".format(
    caption=caption,
    link=raw_link
  )

def github(username):
  return getImageLink(
    "https://github.com/{0}".format(username),
    "GitHub"
  )

def linkedin(username):
  return getImageLink(
    "https://www.linkedin.com/in/{0}".format(username),
    "LinkedIn"
  )

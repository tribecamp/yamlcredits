#
# (c) Tribecamp 2020
# Authored by:
# Kees van Voorthuizen <kees.van.voorthuizen@gmail.com>
# License: MIT
#

# [![Foo](http://www.google.com.au/images/nav_logo7.png)](http://google.com.au/)
def getImageLink(url, img_url, caption):
  """
  Converts a URL to a Markdown image link.
  """
  return "[![{caption}]({img_url} =16x16)]({url})".format(
    caption=caption,
    img_url=img_url,
    url=url
  )

def github(username):
  return getImageLink(
    "https://github.com/{0}".format(username),
    "https://raw.githubusercontent.com/rdimascio/icons/master/icons/github.svg",
    "GitHub"
  )

def linkedin(username):
  return getImageLink(
    "https://www.linkedin.com/in/{0}".format(username),
    "https://raw.githubusercontent.com/rdimascio/icons/master/icons/linkedin.svg",
    "LinkedIn"
  )

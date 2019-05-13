
#!/usr/bin/python

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

import json
import urllib
import sys


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "AIzaSyDXHjrC9DdMV5rG-nI_E0qvWMBn8zaMCVQ"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(topic,best):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
  developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results associated with the
  # specified Freebase topic.
  search_response = youtube.search().list(
    q=topic,
    part="id,snippet",
    maxResults=5
  ).execute()

  videos = []
  i = 1

  # print( the title and ID of each matching resource.
  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      if best is False:
        print( "%d - %s (%s)" % (i, search_result["snippet"]["title"],
        "https://youtube.com/watch?v=" +search_result["id"]["videoId"]))
        print( "\n")
      videos.append("http://youtube.com/watch?v=%s" % search_result["id"]["videoId"])
      i += 1

  return videos


if __name__ == "__main__":
  argparser.add_argument("-q", help="Song name")
  argparser.add_argument("-b", action='store_true', help="Fetch the topmost result")
  args = argparser.parse_args()

  best = getattr(args, 'b')

  if getattr(args, 'q') is None:
    print( "Please provide a valid query string")
    sys.exit(0)

  query = getattr(args, 'q')

  videos = youtube_search(query,best)
  if best is True:
    sys.stdout.write(videos[0])
  else:
    song = raw_input("Enter song number:")
    song = int(song)
    if isinstance(song, int) and song < 5:
      sys.stdout.write(videos[(song-1)])
    else:
      print( "Please enter only number")

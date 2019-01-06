from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys

def search_song(search_criteria):

  client_credentials_manager = SpotifyClientCredentials()
  sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
  results = sp.search(q=search_criteria, limit=10)

  try:
    song_title = results['tracks']['items'][0]['name']
    artist_name = results['tracks']['items'][0]['artists'][0]['name']
    uri = results['tracks']['items'][0]['uri']
    runtime = results['tracks']['items'][0]['duration_ms']
  except:
    song_title = 'yup'
    artist_name = 'this'
    uri = "didn't"
    runtime = 'work'

  return song_title, artist_name, uri, runtime

def upvote(song_name, song_artist, song_number):
  results = open("app/queue.txt", "r")
  data =[]
  queue = []
  with open("app/queue.txt", "r") as f:
    data = f.readlines()

  temp = []
  for d in data:
    try:
      d = d.split(',')
      d[-2] = int(d[-2][1])
      d[-1] = int(d[-1][1])
      queue += [d]
    except:
      "do nothing"
  count = 1
  for q in queue:
    if q[0] == song_name and q[1] == song_artist or count == song_number:
      q[-2] += 1
    count += 1
  with open("app/queue.txt", "w") as f:
    for q in queue:
      write_string = str(q[0]).replace(',','') + ", " + str(q[1][1:]).replace(',','') + ", " + str(q[2][1:]) + ", " + str(q[3][1:]) + ", " + str(q[-2]) + ", " + str(q[-1])# + "\n"
      f.write("%s\n" % write_string)

  pass

def downvote(song_name, song_artist, song_number):
  results = open("app/queue.txt", "r")
  data =[]
  queue = []
  with open("app/queue.txt", "r") as f:
    data = f.readlines()

  temp = []
  for d in data:
    try:
      d = d.split(',')
      d[-2] = int(d[-2][1])
      d[-1] = int(d[-1][1])
      queue += [d]
    except:
      "do nothing"
  count = 1
  for q in queue:
    if q[0] == song_name and q[1] == song_artist or count == song_number:
      q[-2] -= 1
    count += 1
  with open("app/queue.txt", "w") as f:
    for q in queue:
      write_string = str(q[0]).replace(',','') + ", " + str(q[1][1:]).replace(',','') + ", " + str(q[2][1:]) + ", " + str(q[3][1:]) + ", " + str(q[-2]) + ", " + str(q[-1])# + "\n"
      f.write("%s\n" % write_string)

  pass
# upvote('a','b', 1)

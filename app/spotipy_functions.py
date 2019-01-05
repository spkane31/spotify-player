# import spotipy
# import sys
# import spotipy.util as util

# # client_id = 'CLIENT_ID'
# # client_secret = 'CLIENT_SECRET'; // Your secret
# # redirect_uri = 'REDIRECT_URI'; // Your redirect uri
# username = 'spkane31'
# scope = 'user-read-private user-read-playback-state user-modify-playback-state'
# util.prompt_for_user_token(username,scope,client_id='3349955059c54674a3c73197d2a411b1',client_secret='e71c7d81bff0423ca21ee9c5d148da27',redirect_uri='http://localhost:5000/')


# birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
# spotify = spotipy.Spotify()

# results = spotify.artist_albums(birdy_uri, album_type='album')
# albums = results['items']
# while results['next']:
#     results = spotify.next(results)
#     albums.extend(results['items'])

# for album in albums:
#     print(album['name'])

# from spotipy.oauth2 import SpotifyClientCredentials
# import spotipy
# import sys
# import pprint

# if len(sys.argv) > 1:
#     search_str = sys.argv[1]
# else:
#     search_str = 'Kendrick Lamar'

# client_credentials_manager = SpotifyClientCredentials()
# sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
# result = sp.search(search_str)
# # print(result)
# pprint.pprint(result['tracks']['items'][1]['album']['external_urls'])

from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys

def search_song(search_criteria):

  # returns the top search item given an artist

  client_credentials_manager = SpotifyClientCredentials()
  sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

  # artist_name = search_criteria#' '.join(sys.argv[1:])
  results = sp.search(q=search_criteria, limit=1)
  song_title = results['tracks']['items'][0]['name']
  artist_name = results['tracks']['items'][0]['artists'][0]['name']
  uri = results['tracks']['items'][0]['uri']
  runtime = results['tracks']['items'][0]['duration_ms']
  return song_title, artist_name, uri, runtime
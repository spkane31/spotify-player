from flask import render_template
from app import app
import json, requests

from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
import spotipy.util as util

# from keys import lastfm_api_key as key, lastfm_user_name as username
# spotify = spotipy.Spotify()


@app.route('/')
@app.route('/index')
def index():
  # return "Hello, World!"
  return render_template('index.html', title='Home')

@app.route('/get_token')
def get_token():
  username = 'spkane31'
  scope = 'user-read-private user-read-playback-state user-modify-playback-state'
  util.prompt_for_user_token(username,scope,client_id='3349955059c54674a3c73197d2a411b1',client_secret='e71c7d81bff0423ca21ee9c5d148da27',redirect_uri='http://localhost:5000/search')
  client_credentials_manager = SpotifyClientCredentials()
  sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
  # return render_template('get_token.html')


@app.route('/search')
def search():
  # client_credentials_manager = SpotifyClientCredentials()
  # sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
  # search_criteria = 'Kendrick'
  # if len(sys.argv) > 1:
    # artist_name = ' '.join(sys.argv[1:])
  # spotipy.util.prompt_for_user_token(username, scope=None, client_id=None, client_secret=None, redirect_uri=None, cache_path=None)

  # clientID = '3349955059c54674a3c73197d2a411b1'
  # clientSecret = 'e71c7d81bff0423ca21ee9c5d148da27'
  # redirectURL = 'http://localhost:5000/'  # We/Spotify suggest http://localhost:8888/callback/ or http://localhost/
  # # username = 'spkane31'
  # # scope = 'user-read-private user-read-playback-state user-modify-playback-state'
  # # token = util.prompt_for_user_token(username,scope,client_id=clientID,client_secret=clientSecret,redirect_uri=redirectURL)

  # username = 'spkane31'
  # scope = 'user-read-private user-read-playback-state user-modify-playback-state'
  # util.prompt_for_user_token(username,scope,client_id='3349955059c54674a3c73197d2a411b1',client_secret='e71c7d81bff0423ca21ee9c5d148da27',redirect_uri='http://localhost:5000/')
  
  # client_credentials_manager = SpotifyClientCredentials()
  # sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

  # artist_name = 'Kendrick Lamar'
  # results = sp.search(q=artist_name, limit=1)
  # for i, t in enumerate(results['tracks']['items']):
  #   print(' ', i, t['name'])

  # from spotipytest import search_song
  from . import spotipytest

  results = spotipytest.search_song('Kendrick Lamar')

  # results = 'worked'

  return render_template('search.html', results=results)
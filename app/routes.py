from flask import render_template, request, flash, redirect
from app import app
from app.forms import MusicSearchForm
import json, requests

from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys, json
import spotipy.util as util

from . import spotipy_functions
# from . import queueImplementation

@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html', title='Home')

@app.route('/get_token')
def get_token():
  username = 'spkane31'
  scope = 'user-read-private user-read-playback-state user-modify-playback-state'
  util.prompt_for_user_token(username,scope,client_id='3349955059c54674a3c73197d2a411b1',client_secret='e71c7d81bff0423ca21ee9c5d148da27',redirect_uri='http://localhost:5000/search')
  client_credentials_manager = SpotifyClientCredentials()
  sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

@app.route('/search', methods=['GET', 'POST'])
def search():
  search = MusicSearchForm(request.form)
  if request.method == 'POST':
    return search_results(search)
  return render_template('search.html', form=search)


@app.route('/search_results')
def search_results(search):
  results = []
  search_string = search.data['search']
  song_title, artist_name, uri, runtime = spotipy_functions.search_song(search_string)
  write_string = str(song_title).replace(',','') + ", " + str(artist_name).replace(',','') + ", " + str(uri) + ", " + str(runtime) + ", 0, 0\n" 
  with open("app/queue.txt", 'a') as f:
    f.write(write_string)
  return render_template('search_results.html', song=song_title, artist=artist_name, uri=uri, runtime=runtime)
  

@app.route('/search_again', methods=['GET', 'POST'])
def search_again():
  print(request.method)
  if request.method == 'POST':
    if request.form.get('Search') == 'Search':
      print('Searched')
      result = 5
  elif request.method == 'GET':
    print('Not SEARCHED')
    result = 10

  return render_template('search_again.html', result=result)


@app.route('/queue')
def queue():
  # results  = open("app/queue.txt", "r")
  with open("app/queue.txt", "r") as f:
    content = f.readlines()
  results = []
  for c in content:
    c = c.split(',')
    results += [c]
  return render_template('queue.html', results=results)
  
  strings = []
  for r in results:
    stringTemp = r[0] + 'by' + r[1] + 'has a net vote of:' + r[-2] + '-' + r[-1]
    strings += [stringTemp]
  return render_template('queue.html', results=strings, other=results)
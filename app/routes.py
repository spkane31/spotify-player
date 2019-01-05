from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
  # return "Hello, World!"
  return render_template('index.html', title='Home')

@app.route('/search')
def search():
  results = {}
  results['artist'] = "Beyonce"
  results['song'] = "Lemonade"
  return render_template('search.html', results=results)
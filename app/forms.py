from flask_wtf import FlaskForm
from wtforms import Form, StringField, SelectField
from wtforms.validators import DataRequired


class MusicSearchForm(FlaskForm):
  choices = [('Artist', 'Artist'),
               ('Album', 'Album'),
               ('Track', 'Track')]
  select = SelectField('Search for music:', choices=choices)
  search = StringField('') 

class UpvoteButton(FlaskForm):
  choices = [('Upvote', 'Upvote'), ('Downvote', 'Downvote')]
  select = SelectField('Upvote Song #', choices=choices)
  search = StringField('')

class downVoteButton(FlaskForm):
  choices = [('Upvote', 'Upvote'), ('Downvote', 'Downvote')]
  select = SelectField('Upvote Song #', choices=choices)
  search = StringField('')

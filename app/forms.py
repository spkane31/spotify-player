from flask_wtf import FlaskForm
from wtforms import Form, StringField, SelectField
from wtforms.validators import DataRequired


class MusicSearchForm(FlaskForm):
  choices = [('Artist', 'Artist'),
               ('Album', 'Album'),
               ('Track', 'Track')]
  select = SelectField('Search for music:', choices=choices)
  search = StringField('') 

# class VoteButton(FlaskForm):
#   choices = [('Upvote', 'Upvote'), ('Downvote', 'Downvote')]
#   select = SelectedField
from app import app
import urllib.request,json
from .models import movie

Movie = movie.Movie

# Getting api key
api_key = app.config['MOVIE_API_KEY']
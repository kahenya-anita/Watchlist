from flask import render_template
from app import app

# Views
@app.route('/movie/<init:movie_id>')
def movie(movie_id):

    '''
    View movie page function that returns the movie page and its data
    '''
    message = 'Hello world'
    return render_template('movie.html',id = movie_id)
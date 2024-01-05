"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

# from the files we created 
import crud
import model
import server

# python will run dropdb and createdb for us using these commands
os.system("dropdb ratings")
os.system('createdb ratings')

# connect to the database and call db.create_all
model.connect_to_db(server.app)
model.db.create_all()

# load data from data/movies.json and save it to a variable
with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

# Create movies, store them in list so we can use them
# to create fake ratings later
movies_in_db = []
for movie in movie_data:
    # get the title, overview, and poster_path from the movie dictionary
    title, overview, poster_path = (
    movie["title"],
    movie["overview"],
    movie["poster_path"],
    )
    # get the release_date and convert it to a
    # datetime object with datetime.strptime
    release_date = datetime.strptime(movie["release_date"], "%Y-%m-%d")

    # create a movie here and append it to movies_in_db
    db_movie = crud.create_movie(title, overview, release_date, poster_path)
    movies_in_db.append(db_movie)


model.db.session.add_all(movies_in_db)
model.db.session.commit()
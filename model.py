"""Models for movie ratings app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincrement = True,
                        primary_key = True)
    email = db.Column(db.String, unique = True, nullable = False)
    password = db.Column(db.String, nullable = False)

    ratings = db.relationship("Rating", back_populates="user")

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'

class Movie(db.Model):
    """"A Movie."""
    __tablename__ = "movies"

    movie_id = db.Column(db.Integer,
                         autoincrement = True,
                         primary_key = True)
    title = db.Column(db.String)
    overview = db.Column(db.Text)
    release_date = db.Column(db.DateTime)
    poster_path = db.Column(db.String)

    ratings = db.relationship("Rating", back_populates="movie")

    def __repr__(self):
        return f'<Movie movie_id={self.movie_id} title={self.title}>'
    
class Rating(db.Model):
    __tablename__ = "ratings"

    rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    score = db.Column(db.Integer)
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.movie_id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    # a feature of SQLAlchemy

    # a rating has a movie and a user = 2 attributes to rating, movie and user

    # rating.movie will return the movie object related to the rating
    movie = db.relationship("Movie", back_populates="ratings")
    # rating.user will return related User object
    user = db.relationship("User", back_populates="ratings")
    # first argument in db.relationship() is the name of the class this 
    # attribute will be associated with

    # second argument is the name of the attribute that will be used to 
    # reference the related instance(s) of this class

    # back_populates is assigned a value that corresponds to the name of the
    # attribute in the class with the relationship. 



    def __repr__(self):
        return f"<Rating rating_id={self.rating_id} score={self.score}>"

def connect_to_db(flask_app, db_uri="postgresql:///ratings", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)

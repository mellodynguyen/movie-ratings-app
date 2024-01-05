"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db, db
import crud

# StrictUndefined is used to make it throw errors for undefined variables
# (by default, the errors are thrown silently)
from jinja2 import StrictUndefined

app = Flask(__name__)

# the flask instance needs a secret key (otherwise flash and session wont work)
# we also configure Jina2 here
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

# Replace this with routes and view functions!
@app.route('/')
def homepage():
    """"View homepage."""
    
    return render_template('homepage.html')

if __name__ == "__main__":

    app.run(host="0.0.0.0", debug=True)

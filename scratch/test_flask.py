import flask
import os


app = flask.Flask(__name__)


@app.route('/') # Python decorator 
def index(): 
    return "Hello, world!"

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0')
)

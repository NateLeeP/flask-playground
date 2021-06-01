import os
from flask import ( Blueprint, render_template, send_from_directory )

SECRET_KEY = os.environ.get("SECRET_KEY")
greetings = Blueprint('greetings', __name__, url_prefix='/greetings')

@greetings.route('/hello')
def hello():
  return {'greeting': 'Hello World!'}

@greetings.route('/goodbye')
def goodbye():
  return {'greeting': 'So long, sucker!'}

@greetings.route('/about')
def about():
  return render_template('index.html')

@greetings.route('/home')
def home():
  return render_template('index.html')

@greetings.route('/info/<name>')
def info(name):
  return render_template('index.html')

@greetings.route('/')
def landing():
  return render_template('index.html')


#@greetings.route('/', defaults={'path': ''})
##@greetings.route('/<path:path>')
#def home(path):
#  return render_template('index.html')

@greetings.route('/uploads/App')
def upload_javascript():
  return send_from_directory(
    "src", "./App.js", as_attachment=True
  )
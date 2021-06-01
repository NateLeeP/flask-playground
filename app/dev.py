from flask import Flask
from greetings import ( greetings )

app = Flask(__name__, static_url_path="")
app.config.from_pyfile(
        '../config.py')
app.register_blueprint(greetings)




from os import environ
from dotenv import load_dotenv


load_dotenv('.env')


DEBUG = True
TESTING = True
SECRET_KEY = environ.get('SECRET_KEY')
import os
import dotenv as dt

dt.load_dotenv('.env')

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
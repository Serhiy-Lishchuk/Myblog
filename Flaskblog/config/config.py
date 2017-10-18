import configparser
import os

path = os.path.realpath(os.path.dirname(__file__))
config = configparser.ConfigParser()
config.read(os.path.join(path, 'config.ini'))

DATABASE = config.get('PATH', 'DATABASE')
DEBUG = config.get('OTHER', 'DEBUG')
SECRET_KEY = config.get('AUTH', 'SECRET_KEY')
USERNAME = config.get('AUTH', 'USERNAME')
PASSWORD = config.get('AUTH', 'PASSWORD')

APP_DIR = path.rsplit('/Flaskblog', 1)[0]
UPLOAD_MUSIC = os.path.join(APP_DIR, config.get('PATH', 'UPLOAD_MUSIC'))
MUSIC_EXTENSIONS = set(['mp3'])
UPLOAD_IMAGE = os.path.join(APP_DIR, config.get('PATH', 'UPLOAD_IMAGE'))
IMAGE_EXTENSIONS = set(['jpg', 'png'])
MAX_WIDTH = int(config.get('OTHER', 'MAX_WIDTH'))
WATERMARK = os.path.join(APP_DIR, config.get('PATH', 'WATERMARK'))

LOG_NAME = config.get('LOG', 'NAME')
LOG_FILE = config.get('LOG', 'FILENAME')
LOG_LEVEL = config.get('LOG', 'LEVEL')
LOG_FORMAT = config.get('LOG', 'FORMAT')

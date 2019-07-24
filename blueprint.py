import functools

from flask import *
from werkzeug.security import *
from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')
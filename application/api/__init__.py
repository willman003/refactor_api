from flask import Blueprint

api = Blueprint("api",__name__)
api_login = Blueprint("api_login",__name__)

from .views import *
from .authentication import *
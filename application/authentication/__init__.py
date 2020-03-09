from flask import Blueprint

auth_login = Blueprint('auth_login',__name__,template_folder="templates")

from .views import *
from ..models import *
from . import api
from .errors import *

from flask import jsonify, g
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(token):
    if token == '':
        return False
    g.user = Nguoi_dung.verify_auth_token(token)
    
    return True

@api.route('/tokens',methods=['POST'])
@auth.login_required
def get_token():    
    return jsonify({
        'token':g.user.generate_auth_token(expiration=3600),
        'expiration':3600
    })
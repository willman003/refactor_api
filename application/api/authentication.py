from ..models import *
from . import api, api_login
from .errors import *

from flask import jsonify, request, g
from flask_httpauth import HTTPBasicAuth
from flask_httpauth import HTTPTokenAuth

auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()

@auth.verify_password
def verify_password(username, password):
    user = Nguoi_dung.query.filter_by(ten_dang_nhap = username).first()
    if user is None:
        return False
    g.current_user = user
    return user.verify_password(password)

@token_auth.verify_token
def verify_token(token):
    
    g.current_user = Nguoi_dung.check_token(token) if token else None
    
    return g.current_user is not None

@api_login.route('/tokens',methods=['POST'])
@auth.login_required
def get_token():
    token = g.current_user.get_token()
    db.session.commit()
    return jsonify({
        'token':token,
        'expiration':3600
    })

@api.route('/tokens',methods=['DELETE'])
@token_auth.login_required
def revoke_token():
    g.current_user.revoke_token()
    db.session.commit()
    return '', 204

@api.before_request
@token_auth.login_required
def before_request():
    if not g.current_user.is_authenticated :
        return jsonify({
            'status':401,
            'message':'Unauthentication'
        }) 
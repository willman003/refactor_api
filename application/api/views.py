from flask import request, jsonify

from . import api
from ..models import *
from .. import db

import json
import requests

#User resource
@api.route('/users',methods=['GET'])
def get_list_user():
    list_user = Nguoi_dung.query.all()
    
    return json.dumps({
        'users':[user.to_json() for user in list_user]
    },ensure_ascii=False,indent=4)

@api.route('/users/<int:id>',methods=['GET'])
def get_user(id):
    user = Nguoi_dung.query.filter(Nguoi_dung.ma_nguoi_dung == id).first()
    if user:
        return json.dumps({
            "results":user.to_json()
        },ensure_ascii=False,indent=4)
    else:
        return json.dumps({
            "results":"404"
        })

@api.route('/users',methods=['POST'])
def create_user():
    user = Nguoi_dung()

    return json.dumps({
        "result":200
    },ensure_ascii=False,indent=4)


# @api.route('/users/',methods=['POST'])
# def create_product():
#     if not request.json:
#         return json.dumps({
#         "result":400
#         })
#     list_user = Nguoi_dung.query.all()
#     user = User
#     return

#Product resource
@api.route('/products',methods=['GET'])
def get_list_product():
    products = San_pham.query.all()
    
    return json.dumps({
        'products':[product.to_json() for product in products]
    },ensure_ascii=False,indent=4)

@api.route('/products/<int:id>',methods=['GET'])
def get_product(id):
    product = San_pham.query.filter(San_pham.ma_san_pham==id).first()
    if product:
        return json.dumps({
        'result':product.to_json()
    },ensure_ascii=False,indent=4)
    else:
        return json.dumps({
            "result":404
        })

# @api.route('/products/<int:id>',methods=['GET'])
# def get_product(id):
#     product = San_pham.query.filter(San_pham.ma_san_pham==id).first()
#     if product:
#         return jsonify({
#         'result':product.to_json()
#     })
#     else:
#         return jsonify({
#             "result":404
#         })


#Order resource

#Order's detail resource
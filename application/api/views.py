from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

from datetime import datetime

from . import api, api_login

from ..models import *
from .. import db

message = {
    "version":1.0,
    "status":200,
    "message":"Successful",
    "result":None,
}



#User resource
@api.route('/users',methods=['GET'])
def get_list_user():
    list_user = Nguoi_dung.query.all()
    message['result'] = [user.to_json() for user in list_user]
    message['status'] = 200
    message['message'] = "Successful"
    
    return jsonify(message)

@api.route('/users/<int:id>',methods=['GET'])
def get_user(id):
    user = Nguoi_dung.query.filter(Nguoi_dung.ma_nguoi_dung == id).first()
    if user:
        message['result'] = user.to_json()        
    else:
        message['status'] = 404
        message['message'] = "Resources Not Found"
    return jsonify(message)

@api.route('/users',methods=['POST'])
def create_user():
    item = request.get_json()
    user = Nguoi_dung()
    user.ho_ten = item['name']
    user.ten_dang_nhap = item['username']
    user.mat_khau_hash = item['password']
    user.ma_loai_nguoi_dung = 1
    db.session.add(user)
    db.session.commit()
    item['id'] = user.get_id()
    item.pop('password')    
    message['status'] = 200
    message['message'] = 'Successfully Created'
    message['result'] = item
    return jsonify(message)

@api.route('/users/<int:id>',methods=['PUT'])
def edit_user(id):
    user = Nguoi_dung.query.filter(Nguoi_dung.ma_nguoi_dung == id).first()
    if user:
        item = request.get_json()
        message['result'] = {}
        message['result']['before'] = user.to_json()
        user.ho_ten = item['name']
        user.ten_dang_nhap = item['username']
        user.mat_khau_hash = item['password']
        db.session.add(user)
        db.session.commit()
        message['status'] = 200
        message['message'] = 'Successfully Editted User #' + str(user.get_id())
        message['result']['after'] = user.to_json()

    else:
        message['status'] = 404
        message['message'] = "Resources Not Found"
    return jsonify(message)

@api.route('/users/<int:id>',methods=['DELETE'])
def delete_user(id):
    user = Nguoi_dung.query.filter(Nguoi_dung.ma_nguoi_dung == id).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        message['status'] = 200
        message['message'] = "Successfully Deleted"
        message['result'] ={
            "id":user.get_id(),
            "username":user.ten_dang_nhap
        } 
        
    else:
        message['status'] = 404
        message['message'] = 'Resources Not Found'
    return jsonify(message)

#Customer resource
@api.route('/customers',methods=['GET'])
def get_list_customers():
    list_customers = Khach_hang.query.all()
    message['result'] = [customer.to_json() for customer in list_customers]
    message['status'] = 200
    return jsonify(message)

@api.route('/customers/<int:id>',methods=['GET'])
def get_customer(id):
    customer = Khach_hang.query.filter_by(ma_khach_hang=id).first()
    if customer:
        message['result'] = customer.to_json()
        message['status'] = 200
    else:
        message['status'] = 404
        message['message'] = "Resourcs Not Found"
    return jsonify(message)


@api.route('/customers',methods=['POST'])
def create_customer():
    item = request.get_json()
    customer = Khach_hang()
    customer.ten_khach_hang = item['name']
    customer.email = item['email']
    customer.dia_chi = item['address']
    customer.dien_thoai = item['phone']
    customer.ten_dang_nhap = item['username']
    customer.mat_khau_hash= generate_password_hash(item['password'])
    customer.access_level = 0
    db.session.add(customer)
    db.session.commit()
    item['id'] = customer.get_id()
    message['status'] = 200
    message['message'] = 'Successfully Created'
    message['result'] = item
    return jsonify(message)

#Product resource
@api.route('/products',methods=['GET'])
def get_list_product():
    products = San_pham.query.all()
    message['result'] = [product.to_json() for product in products]
    return jsonify(message)

@api.route('/products/<int:id>',methods=['GET'])
def get_product(id):
    product = San_pham.query.filter(San_pham.ma_san_pham==id).first()
    if product:
        message['result'] = product.to_json() 
    else:
        message['status'] = 404
        message['message'] = 'Resources Not Found'
    return jsonify(message)

@api.route('/products/categories',methods=['GET'])
def get_product_category():
    list_category = Loai_san_pham.query.all()
    message['result'] = [category.to_json() for category in list_category]
    return jsonify(message)

@api.route('/products/categories/<int:id>',methods=['GET'])
def get_category_name(id):
    category = Loai_san_pham.query.filter_by(ma_loai=id).first()
    if category:
        message['result'] = category.to_json()
    else:
        message['status'] = 404
        message['message'] = "Resources Not Found"
    return jsonify(message)


@api.route('/products',methods=['POST'])
def create_product():
    item = request.get_json()
    product = San_pham()
    product.ten_san_pham = item['product_name'].upper()
    product.ma_loai = item['product_category']
    product.gia_ban = item['price']
    product.gia_nhap = item['stock_price']
    product.so_luong_ton = item['quantity']
    product.mo_ta = item['description']
    db.session.add(product)
    db.session.commit()
    item['id'] = product.get_id()
    message['status'] = 200
    message['message'] = 'Successfully Created'
    message['result'] = item
    return jsonify(message)

@api.route('/products/<int:id>',methods=['PUT'])
def edit_product(id):
    product = San_pham.query.filter(San_pham.ma_san_pham==id).first()
    if product:
        item = request.get_json()
        message['result'] = {}
        message['result']['before'] = product.to_json()
        product.ten_san_pham = item['product_name'].upper()
        product.gia_ban = item['price']
        product.gia_nhap = item['stock_price']
        product.so_luong_ton = item['quantity']
        db.session.add(product)
        db.session.commit()
        message['status'] = 200
        message['message'] = 'Successfully Editted User #' + str(product.get_id())
        message['result']['after'] = product.to_json()
    else:
        message['status'] = 404
        message['message'] = 'Resources Not Found'

    return jsonify(message)

@api.route('/products/<int:id>',methods=['DELETE'])
def delete_product(id):
    product = San_pham.query.filter(San_pham.ma_san_pham==id).first()
    if product:
        db.session.delete(product)
        db.session.commit()
        message['status'] = 200
        message['message'] = 'Successfully Deleted Product #' + str(product.get_id())
    else:
        message['status'] = 404
        message['message'] = 'Resources Not Found'

    return jsonify(message)

#Order resource

@api.route('/orders',methods=['GET'])
def get_list_order():
    list_order = Hoa_don.query.order_by(Hoa_don.ngay_tao_hoa_don).all()
    message['result'] = [order.to_json() for order in list_order]
    for item in message['result']:
        list_detail = Don_hang.query.filter(Don_hang.ma_hoa_don == item['order_id']).all()
        item['detail'] = [detail.to_json() for detail in list_detail]
    message['status'] = 200
    
    return jsonify(message)

@api.route('/orders/<int:id>',methods=['GET'])
def get_order(id):
    order = Hoa_don.query.get(id)
    list_detail = Don_hang.query.filter(Don_hang.ma_hoa_don==id).all()
    if order:
        message['status'] = 200
        message['message'] = "Successful"
        message['result'] = order.to_json()
        message['result']['detail'] = [detail.to_json() for detail in list_detail]
    else:
        message['status'] = 404
        message['message'] = 'Resources Not Found'
    return jsonify(message)

@api.route('/orders',methods=['POST'])
def create_order():
    item = request.get_json()
    order = Hoa_don()
    customer = Khach_hang()
    try:
        order.ngay_tao_hoa_don = datetime.now()
        customer.ten_khach_hang = item['customer_name']
        customer.dia_chi = item['customer_address']
        customer.dien_thoai = item['customer_phone']
        customer.email = item['customer_email']
        db.session.add(customer)
        db.session.commit()
        order.ma_khach_hang = customer.get_id()
        order.tong_tien = item['total']
        order.giam_gia = item['discount']
        order.kenh_ban = item['sale_channel']
        order.ma_hoa_don_kenh_ban = item['channel_order_id']
        order.nha_van_chuyen = item['delivery']
        order.phi_van_chuyen = item['shipping_fee']
        order.ma_van_don = item['tracking_number']
        order.trang_thai = item['status']
        db.session.add(order)
        db.session.commit()
        message['result'] = {
            'order_id':order.get_id(),
            'total':item['total']
        }
        message['status'] = 200
        message['message'] = "Successfully"
    except KeyError:
        message['status'] = 500
        message['message'] = 'Not Sufficient Parameter'

    return jsonify(message)

@api.route('/orders/<int:id>',methods=['DELETE'])
def delete_order(id):
    order = Hoa_don.query.filter(Hoa_don.ma_hoa_don == id).first()
    if order:
        ma_id = order.get_id()
        db.session.delete(order)
        db.session.commit()
        message['status'] = 200
        message['message'] = "Successfully Deleted Order #" + str(ma_id)
    else:
        message['status'] = 404
        message['message'] = "Resources Not Found"
    return jsonify(message)

#Order's detail resource
@api.route('/orders/<int:id>',methods=['POST'])
def create_order_detail(id):
    order = Hoa_don.query.filter(Hoa_don.ma_hoa_don == id).first()
    if order:
        list_detail = Don_hang.query.filter(Don_hang.ma_hoa_don==id).all()
        item = request.get_json()
        try:            
            product = San_pham.query.filter(San_pham.ma_san_pham==item['product_id']).first()
            if product:
                list_product = [item.ma_san_pham for item in list_detail]
                if item['product_id'] in list_product:
                    detail = Don_hang.query.filter(Don_hang.ma_san_pham == item['product_id']).first()
                    detail.so_luong += item['quantity']
                    db.session.add(detail)
                    db.session.commit()
                    message['result'] = detail.to_json()
                    message['result']['add'] = item['quantity']
                else:
                    detail = Don_hang()
                    detail.ma_hoa_don = id
                    detail.ma_san_pham = item['product_id']
                    detail.so_luong = item['quantity']
                    detail.ten_san_pham = product.ten_san_pham
                    detail.gia_ban = product.gia_ban
                    detail.gia_nhap = product.gia_nhap
                    detail.loi_nhuan = (detail.gia_ban-detail.gia_nhap)*detail.so_luong
                    db.session.add(detail)
                    db.session.commit()
                    message['status'] = 200
                    message['message'] = "Successfully Add Detail for Order #" + str(id)
                    message['result'] = detail.to_json()
            else:
                message['status'] = 500
                message['message'] = "Error: Product Not Existed"
        except KeyError:
            message['status'] = 500
            message['message'] = "Not Sufficient Parameter"
        

                    
    else:
        message['status'] = 404
        message['message'] = "Resources Not Found"
    return jsonify(message)

@api.route('/orders/<int:id>/<int:prod_id>', methods=['DELETE'])
def delete_order_detail(id, prod_id):
    list_detail = Don_hang.query.filter(Don_hang.ma_hoa_don == id).all()
    if len(list_detail)>0:
        for item in list_detail:
            if item.ma_san_pham == prod_id:
                db.session.delete(item)
                db.session.commit()
                message['status'] = 200
                message['message'] = "Successfully Deleted Item #" +str(prod_id)+" in Order #" +str(id)
                break
        else:
            message['status'] = 500
            message['message'] = "Error: Product Not Existed"
    else:
        message['status'] = 404
        message['message'] = "Resources Not Found"
    return jsonify(message)
from . import main
from ..api_handler.handler import *
from .forms import *

from flask import render_template, redirect, url_for,jsonify,session

@main.route('/',methods=['GET','POST'])
def index():
    list_product = api_get_list_products()
    dict_category = {}
    for item in api_get_list_category():
        dict_category[item['category_id']] = item['category_name']
                
    return render_template('index.html', list_product = list_product, dict_category = dict_category)

@main.route('/add-products',methods=['GET','POST'])
def create_product():
    form = Form_tao_san_pham()
    thong_bao = ''
    lst_select = []
    for item in api_get_list_category():
        tup_temp = (str(item['category_id']),item['category_name'])
        lst_select.append(tup_temp)
    form.ten_loai.choices = lst_select
    
    if form.validate_on_submit():
        status = api_create_product(form.ten_san_pham.data,
            int(form.ten_loai.data),
            form.gia_ban.data,
            form.gia_nhap.data,
            form.so_luong_ton.data,
            form.mo_ta.data)
        if status == 200:
            thong_bao = 'Tạo thành công'
    return render_template('create_new_product.html',form=form,thong_bao=thong_bao)

@main.route('/wallets/<int:id>',methods=['GET','POST'])
def product_detail(id):
    form = Form_mua_hang()
    product = api_get_product(id)
    list_product = api_get_list_products()
    dict_category = {}
    for item in api_get_list_category():
        dict_category[item['category_id']] = item['category_name']
    

    return render_template('product_detail.html', list_product = list_product, product = product, dict_category = dict_category, form = form)


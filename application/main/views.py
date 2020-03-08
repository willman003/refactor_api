from . import main
from ..api_handler.handler import *
from .forms import *

from flask import render_template, redirect, url_for,jsonify

@main.route('/',methods=['GET','POST'])
def index():
    
    return render_template('index.html')

@main.route('/add-products',methods=['GET','POST'])
def create_product():
    form = Form_tao_san_pham()
    thong_bao = ''
    lst_select = []
    for item in api_get_category():
        tup_temp = (item['category_id'],item['category_name'])
        lst_select.append(tup_temp)
    form.ten_loai.choices = lst_select
    
    if form.validate_on_submit():
        status = api_create_product(form.ten_san_pham.data,
            form.gia_ban.data,
            form.gia_nhap.data,
            form.so_luong_ton.data)
        if status == 200:
            thong_bao = 'Tạo thành công'
    

    return render_template('Tao_san_pham_moi.html',form=form,thong_bao=thong_bao)
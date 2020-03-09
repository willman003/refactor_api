from . import auth_login
from .forms import *
from ..api_handler.handler import *

from flask import render_template, redirect, url_for, session

from werkzeug.security import check_password_hash

@auth_login.route('/login',methods=['GET','POST'])
def login():
    form = Form_dang_nhap()
    list_customers = api_get_list_customer()
    thong_bao = ''
    if form.validate_on_submit():
        for user in list_customers:
            if user['customer_username'] == form.ten_dang_nhap.data and check_password_hash(user['customer_password'],form.mat_khau.data):
                session['customer'] = user
                return redirect(url_for('main.index'))
            else:
                thong_bao = 'Tên đăng nhập hoặc Mật khẩu không chính xác!'               

    return render_template('login.html', form = form,thong_bao=thong_bao)

@auth_login.route('/register',methods=['GET','POST'])
def register():
    form = Form_dang_ky()
    status = ''
    if form.validate_on_submit():
        status = api_create_customer(form.ten_khach_hang.data,
            form.email.data,
            form.dia_chi.data,
            form.dien_thoai.data,
            form.ten_dang_nhap.data,
            form.mat_khau.data)
        
    return render_template('register.html', form = form, status = status)

@auth_login.route('/logout',methods=['GET','POST'])
def logout():
    session.clear()
    return redirect(url_for('main.index'))
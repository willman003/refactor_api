from flask_wtf import FlaskForm
from wtforms import fields, validators

class Form_dang_nhap(FlaskForm):
    ten_dang_nhap = fields.StringField('Tên đăng nhập:', [validators.required()])
    mat_khau = fields.StringField('Mật khẩu:', [validators.required()])
    submit = fields.SubmitField('Đăng nhập')

class Form_dang_ky(FlaskForm):
    ten_khach_hang = fields.StringField('Tên của bạn:')
    email = fields.StringField('Email:')
    dia_chi = fields.StringField('Địa chỉ giao hàng:')
    dien_thoai = fields.StringField('Điện thoại:')
    ten_dang_nhap = fields.StringField('Tên đăng nhập:')
    mat_khau = fields.StringField('Mật khẩu')
    submit = fields.SubmitField('Đăng ký')

class Form_cap_nhat(FlaskForm):
    ten_khach_hang = fields.StringField('Tên của bạn:')
    email = fields.StringField('Email:')
    dia_chi = fields.StringField('Địa chỉ giao hàng:')
    dien_thoai = fields.StringField('Điện thoại:')
    ten_dang_nhap = fields.StringField('Tên đăng nhập:')
    mat_khau = fields.StringField('Mật khẩu')
    submit = fields.SubmitField('Cập nhật thông tin')
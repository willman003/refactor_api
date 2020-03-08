from flask_wtf import FlaskForm
from wtforms import fields,validators


class Form_tao_san_pham(FlaskForm):
    ten_san_pham = fields.StringField('Tên sản phẩm:', [validators.required('Tên sản phẩm bỏ trống')])
    ten_loai = fields.SelectField('Loại:', [validators.required('Tên sản phẩm bỏ trống')])
    gia_ban = fields.IntegerField('Giá bán:', [validators.required('Giá bán bỏ trống')])
    gia_nhap = fields.IntegerField('Giá nhập:',[validators.required('Giá nhập bỏ trống')])
    thuoc_tinh = fields.TextField('Thuộc tính:')
    mo_ta = fields.TextField('Mô tả:')
    so_luong_ton = fields.IntegerField('Số lượng: ')
    submit = fields.SubmitField('Tạo')
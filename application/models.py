from . import db

from werkzeug.security import generate_password_hash, check_password_hash
import base64
from datetime import datetime, timedelta
import os

#------CLASS cho Web bán hàng------#
class Loai_san_pham(db.Model):
    __tablename__ = 'loai_san_pham'
    ma_loai = db.Column(db.Integer, nullable = False, primary_key = True)
    ten_loai = db.Column(db.String(50), nullable = False)
    mo_ta = db.Column(db.Text)
    
    def __str__(self):
        return self.ten_loai

class San_pham(db.Model):
    __tablename__ = 'san_pham'
    ma_san_pham = db.Column(db.Integer, nullable = False, primary_key = True)
    ten_san_pham = db.Column(db.String(100), nullable = False)
    ma_loai = db.Column(db.Integer, db.ForeignKey('loai_san_pham.ma_loai'))
    gia_ban = db.Column(db.Integer, nullable = False)
    gia_nhap = db.Column(db.Integer, nullable = False, default = 0)
    so_luong_ton = db.Column(db.Integer, nullable = False, default = 0)
    id_sendo = db.Column(db.Integer)
    thuoc_tinh = db.Column(db.String(200))
    current_nhap_hang = db.Column(db.String(200))
    current_edit_price = db.Column(db.String(200))
    
    loai_san_pham = db.relationship(Loai_san_pham, backref=db.backref('san_pham', lazy = 'joined'))
    def __str__(self):
        return self.ten_san_pham

    def get_id(self):
        return self.ma_san_pham
    
    def to_json(self):
        json_product = {
            "id":self.ma_san_pham,
            "name":self.ten_san_pham,
            "category":self.ma_loai,
            "import_price":self.gia_ban,
            "sell_price":self.gia_nhap,
            "stock_quantity":self.so_luong_ton
        }
        return json_product
    

    
    
class Loai_nguoi_dung(db.Model):
    __tablename__ = 'loai_nguoi_dung'
    ma_loai_nguoi_dung = db.Column(db.Integer, nullable = False, primary_key = True)
    ten_loai_nguoi_dung = db.Column(db.String(100))
    def __str__(self):
        return self.ten_loai_nguoi_dung


class Nguoi_dung(db.Model):
    __tablename__ = 'nguoi_dung'
    ma_nguoi_dung = db.Column(db.Integer, nullable = False, primary_key = True)
    ma_loai_nguoi_dung = db.Column(db.Integer, db.ForeignKey('loai_nguoi_dung.ma_loai_nguoi_dung'))
    ho_ten = db.Column(db.String(200))
    ten_dang_nhap = db.Column(db.String(64), nullable = False)
    mat_khau_hash = db.Column(db.String(128), nullable = False)
    token = db.Column(db.String(32), index=True, unique=True)
    token_expiration = db.Column(db.DateTime)

    loai_nguoi_dung = db.relationship(Loai_nguoi_dung,backref=db.backref('nguoi_dung',lazy='joined')) 
    @property
    def is_authenticated(self):
        return True
    @property
    def is_active(self):
        return True
    @property
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return self.ma_nguoi_dung

    def __unicode__(self):
        return self.ho_ten
    
    def __str__(self):
        return self.ten_dang_nhap

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def set_password(self, password):
        self.mat_khau_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.mat_khau_hash, password)

    def get_token(self,expiration=3600):
        now = datetime.utcnow()
        if self.token and self.token_expiration > now + timedelta(seconds=60):
            return self.token
        self.token = base64.b64encode(os.urandom(24)).decode('utf-8')
        self.token_expiration = now + timedelta(seconds=expiration)
        db.session.add(self)
        return self.token

    def revoke_token(self):
        self.token_expiration = datetime.utcnow() - timedelta(seconds=1)

    @staticmethod
    def check_token(token):
        user = Nguoi_dung.query.filter(Nguoi_dung.token== token).first()
        
        if user is None or user.token_expiration < datetime.utcnow():
            return None
        return user

    def to_json(self):
        json_user = {
            "user_id":self.ma_nguoi_dung,
            "access_level":self.ma_loai_nguoi_dung,
            "name":self.ho_ten,
            "username":self.ten_dang_nhap
            
        }
        return json_user
   
    



class Khach_hang(db.Model):
    __tablename__ = 'khach_hang'
    ma_khach_hang = db.Column(db.Integer, nullable = False, primary_key = True)
    ten_khach_hang = db.Column(db.String(100))
    email = db.Column(db.String(100))
    dia_chi = db.Column(db.String(200))
    dien_thoai = db.Column(db.String(20))
    
    def __str__(self):
        return self.dia_chi

    def get_id(self):
        return self.ma_khach_hang
    
class Hoa_don(db.Model):
    __tablename__ = 'hoa_don'
    ma_hoa_don = db.Column(db.Integer, nullable = False, primary_key = True)
    ngay_tao_hoa_don = db.Column(db.DateTime, nullable = False)
    ma_khach_hang = db.Column(db.Integer, db.ForeignKey('khach_hang.ma_khach_hang'))
    tong_tien = db.Column(db.Float, nullable = False)
    giam_gia = db.Column(db.Float, default = 0)
    kenh_ban = db.Column(db.String(100))
    ma_hoa_don_kenh_ban = db.Column(db.String(50))
    nha_van_chuyen = db.Column(db.String(255))
    phi_van_chuyen = db.Column(db.Float)
    ma_van_don = db.Column(db.String(100))
    trang_thai = db.Column(db.Integer)
    ghi_chu = db.Column(db.Text)
    da_in_hd = db.Column(db.Integer, default = 0)
    da_cap_nhat_kho = db.Column(db.Integer, default = 0)
    
    khach_hang = db.relationship(Khach_hang, backref = db.backref('hoa_don',lazy='joined'))
    def __repr__(self):
        return "<Ma_hoa_don = %d>" % self.ma_hoa_don

    def get_id(self):
        return self.ma_hoa_don

    def to_json(self):
        json_order = {
            "order_id" : self.ma_hoa_don,
            "date": self.ngay_tao_hoa_don.strftime("%d-%m-%Y %H:%M:%S"),
            "customer": self.ma_khach_hang,
            "total":self.tong_tien,
            "discount":self.giam_gia,
            "sale_channel":self.kenh_ban,
            "order_id_by_channel":self.ma_hoa_don_kenh_ban,
            "delivery":self.nha_van_chuyen,
            "shipping_code":self.ma_van_don,
            "status":self.trang_thai
        }
        return json_order

class Don_hang(db.Model):
    __tablename__ = 'don_hang'
    id = db.Column(db.Integer, nullable =False, primary_key = True)
    ma_hoa_don = db.Column(db.Integer, db.ForeignKey('hoa_don.ma_hoa_don'))
    ma_san_pham = db.Column(db.Integer)
    ten_san_pham = db.Column(db.String(100), nullable = False)
    so_luong = db.Column(db.Integer, nullable = False)
    gia_ban = db.Column(db.Integer)
    gia_nhap = db.Column(db.Integer)
    ghi_chu = db.Column(db.Text)
    loi_nhuan = db.Column(db.Integer)
    hoa_don = db.relationship(Hoa_don, backref = db.backref('don_hang',lazy='joined'), foreign_keys=[ma_hoa_don])
    
    def __repr__(self):
        return "<Ma_hoa_don = %d>" % self.ma_hoa_don

    def to_json(self):
        json_detail = {
            "product_id":self.ma_san_pham,
            "product_name":self.ten_san_pham,
            "quantity":self.so_luong,
            "price":self.gia_ban
        }
        return json_detail

class Thu_chi(db.Model):
    __tablename__ = 'thu_chi'
    id = db.Column(db.Integer, nullable = False, primary_key = True)
    ten = db.Column(db.String(200), nullable = False)
    noi_dung = db.Column(db.Text)
    so_tien = db.Column(db.Float, nullable = False)
    thoi_gian = db.Column(db.DateTime)
    loai = db.Column(db.Integer)

    def __str__(self):
        return self.ten
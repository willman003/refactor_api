"""empty message

Revision ID: a313c10e92e3
Revises: b15a557e323f
Create Date: 2020-03-04 16:02:17.547120

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a313c10e92e3'
down_revision = 'b15a557e323f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('don_hang')
    op.drop_table('san_pham')
    op.drop_table('thu_chi')
    op.drop_table('hoa_don')
    op.drop_table('loai_san_pham')
    op.drop_table('khach_hang')
    op.drop_table('loai_nguoi_dung')
    op.drop_table('nguoi_dung')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('nguoi_dung',
    sa.Column('ma_nguoi_dung', sa.INTEGER(), nullable=False),
    sa.Column('ma_loai_nguoi_dung', sa.INTEGER(), nullable=True),
    sa.Column('ho_ten', sa.VARCHAR(length=200), nullable=True),
    sa.Column('ten_dang_nhap', sa.VARCHAR(length=64), nullable=False),
    sa.Column('mat_khau_hash', sa.VARCHAR(length=128), nullable=False),
    sa.ForeignKeyConstraint(['ma_loai_nguoi_dung'], ['loai_nguoi_dung.ma_loai_nguoi_dung'], ),
    sa.PrimaryKeyConstraint('ma_nguoi_dung')
    )
    op.create_table('loai_nguoi_dung',
    sa.Column('ma_loai_nguoi_dung', sa.INTEGER(), nullable=False),
    sa.Column('ten_loai_nguoi_dung', sa.VARCHAR(length=100), nullable=True),
    sa.PrimaryKeyConstraint('ma_loai_nguoi_dung')
    )
    op.create_table('khach_hang',
    sa.Column('ma_khach_hang', sa.INTEGER(), nullable=False),
    sa.Column('ten_khach_hang', sa.VARCHAR(length=100), nullable=True),
    sa.Column('email', sa.VARCHAR(length=100), nullable=True),
    sa.Column('dia_chi', sa.VARCHAR(length=200), nullable=True),
    sa.Column('dien_thoai', sa.VARCHAR(length=20), nullable=True),
    sa.PrimaryKeyConstraint('ma_khach_hang')
    )
    op.create_table('loai_san_pham',
    sa.Column('ma_loai', sa.INTEGER(), nullable=False),
    sa.Column('ten_loai', sa.VARCHAR(length=50), nullable=False),
    sa.Column('mo_ta', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('ma_loai')
    )
    op.create_table('hoa_don',
    sa.Column('ma_hoa_don', sa.INTEGER(), nullable=False),
    sa.Column('ngay_tao_hoa_don', sa.DATETIME(), nullable=False),
    sa.Column('ma_khach_hang', sa.INTEGER(), nullable=True),
    sa.Column('tong_tien', sa.FLOAT(), nullable=False),
    sa.Column('giam_gia', sa.FLOAT(), nullable=True),
    sa.Column('kenh_ban', sa.VARCHAR(length=100), nullable=True),
    sa.Column('ma_hoa_don_kenh_ban', sa.VARCHAR(length=50), nullable=True),
    sa.Column('nha_van_chuyen', sa.VARCHAR(length=255), nullable=True),
    sa.Column('phi_van_chuyen', sa.FLOAT(), nullable=True),
    sa.Column('ma_van_don', sa.VARCHAR(length=100), nullable=True),
    sa.Column('trang_thai', sa.INTEGER(), nullable=True),
    sa.Column('ghi_chu', sa.TEXT(), nullable=True),
    sa.Column('da_in_hd', sa.INTEGER(), nullable=True),
    sa.Column('da_cap_nhat_kho', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['ma_khach_hang'], ['khach_hang.ma_khach_hang'], ),
    sa.PrimaryKeyConstraint('ma_hoa_don')
    )
    op.create_table('thu_chi',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('ten', sa.VARCHAR(length=200), nullable=False),
    sa.Column('noi_dung', sa.TEXT(), nullable=True),
    sa.Column('so_tien', sa.FLOAT(), nullable=False),
    sa.Column('thoi_gian', sa.DATETIME(), nullable=True),
    sa.Column('loai', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('san_pham',
    sa.Column('ma_san_pham', sa.INTEGER(), nullable=False),
    sa.Column('ten_san_pham', sa.VARCHAR(length=100), nullable=False),
    sa.Column('ma_loai', sa.INTEGER(), nullable=True),
    sa.Column('gia_ban', sa.INTEGER(), nullable=False),
    sa.Column('gia_nhap', sa.INTEGER(), nullable=False),
    sa.Column('so_luong_ton', sa.INTEGER(), nullable=False),
    sa.Column('id_sendo', sa.INTEGER(), nullable=True),
    sa.Column('thuoc_tinh', sa.VARCHAR(length=200), nullable=True),
    sa.Column('current_nhap_hang', sa.VARCHAR(length=200), nullable=True),
    sa.Column('current_edit_price', sa.VARCHAR(length=200), nullable=True),
    sa.ForeignKeyConstraint(['ma_loai'], ['loai_san_pham.ma_loai'], ),
    sa.PrimaryKeyConstraint('ma_san_pham')
    )
    op.create_table('don_hang',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('ma_hoa_don', sa.INTEGER(), nullable=True),
    sa.Column('ma_san_pham', sa.INTEGER(), nullable=True),
    sa.Column('ten_san_pham', sa.VARCHAR(length=100), nullable=False),
    sa.Column('so_luong', sa.INTEGER(), nullable=False),
    sa.Column('gia_ban', sa.INTEGER(), nullable=True),
    sa.Column('gia_nhap', sa.INTEGER(), nullable=True),
    sa.Column('ghi_chu', sa.TEXT(), nullable=True),
    sa.Column('loi_nhuan', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['ma_hoa_don'], ['hoa_don.ma_hoa_don'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
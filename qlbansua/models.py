from django.db import models

# Create your models here.


class HangSua(models.Model):
    # Field name made lowercase.
    ma_hang_sua = models.CharField(
        db_column='Ma_hang_sua', primary_key=True, max_length=20)
    # Field name made lowercase.
    ten_hang_sua = models.CharField(db_column='Ten_hang_sua', max_length=100)
    # Field name made lowercase.
    dia_chi = models.CharField(db_column='Dia_chi', max_length=200)
    # Field name made lowercase.
    dien_thoai = models.CharField(db_column='Dien_thoai', max_length=20)
    # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100)

    class Meta:
        managed = False
        db_table = 'hang_sua'


class LoaiSua(models.Model):
    # Field name made lowercase.
    ma_loai_sua = models.CharField(
        db_column='Ma_loai_sua', primary_key=True, max_length=3)
    # Field name made lowercase.
    ten_loai = models.CharField(db_column='Ten_loai', max_length=50)

    class Meta:
        managed = False
        db_table = 'loai_sua'


class Sua(models.Model):
    # Field name made lowercase.
    ma_sua = models.CharField(
        db_column='Ma_sua', primary_key=True, max_length=6)
    # Field name made lowercase.
    ten_sua = models.CharField(db_column='Ten_sua', max_length=100)
    # Field name made lowercase.
    ma_hang_sua = models.ForeignKey(
        HangSua, models.DO_NOTHING, db_column='Ma_hang_sua')
    # Field name made lowercase.
    ma_loai_sua = models.ForeignKey(
        LoaiSua, models.DO_NOTHING, db_column='Ma_loai_sua')
    # Field name made lowercase.
    trong_luong = models.IntegerField(db_column='Trong_luong')
    # Field name made lowercase.
    don_gia = models.IntegerField(db_column='Don_gia')
    # Field name made lowercase.
    tp_dinh_duong = models.TextField(db_column='Tp_dinh_duong')
    # Field name made lowercase.
    loi_ich = models.TextField(db_column='Loi_ich')
    # Field name made lowercase.
    hinh = models.CharField(db_column='Hinh', max_length=200)

    class Meta:
        managed = False
        db_table = 'sua'


class KhachHang(models.Model):
    # Field name made lowercase.
    ma_khach_hang = models.CharField(
        db_column='Ma_khach_hang', primary_key=True, max_length=5)
    # Field name made lowercase.
    ten_khach_hang = models.CharField(
        db_column='Ten_khach_hang', max_length=100)
    phai = models.IntegerField(db_column='Phai')  # Field name made lowercase.
    # Field name made lowercase.
    dia_chi = models.CharField(db_column='Dia_chi', max_length=200)
    # Field name made lowercase.
    dien_thoai = models.CharField(db_column='Dien_thoai', max_length=20)
    # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100)

    class Meta:
        managed = False
        db_table = 'khach_hang'


class CtHoadon(models.Model):
    # Field name made lowercase.
    so_hoa_don = models.OneToOneField(
        'HoaDon', models.DO_NOTHING, db_column='So_hoa_don', primary_key=True)
    # Field name made lowercase.
    ma_sua = models.ForeignKey('Sua', models.DO_NOTHING, db_column='Ma_sua')
    # Field name made lowercase.
    so_luong = models.IntegerField(db_column='So_luong')
    # Field name made lowercase.
    don_gia = models.IntegerField(db_column='Don_gia')

    class Meta:
        managed = False
        db_table = 'ct_hoadon'
        unique_together = (('so_hoa_don', 'ma_sua'),)


class HoaDon(models.Model):
    # Field name made lowercase.
    so_hoa_don = models.CharField(
        db_column='So_hoa_don', primary_key=True, max_length=5)
    # Field name made lowercase.
    ngay_hd = models.DateField(db_column='Ngay_HD')
    # Field name made lowercase.
    ma_khach_hang = models.ForeignKey(
        'KhachHang', models.DO_NOTHING, db_column='Ma_khach_hang')
    # Field name made lowercase.
    tri_gia = models.FloatField(db_column='Tri_gia')

    class Meta:
        managed = False
        db_table = 'hoa_don'

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CtHoadon(models.Model):
    so_hoa_don = models.OneToOneField('HoaDon', models.DO_NOTHING, db_column='So_hoa_don', primary_key=True)  # Field name made lowercase.
    ma_sua = models.ForeignKey('Sua', models.DO_NOTHING, db_column='Ma_sua')  # Field name made lowercase.
    so_luong = models.IntegerField(db_column='So_luong')  # Field name made lowercase.
    don_gia = models.IntegerField(db_column='Don_gia')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ct_hoadon'
        unique_together = (('so_hoa_don', 'ma_sua'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class HangSua(models.Model):
    ma_hang_sua = models.CharField(db_column='Ma_hang_sua', primary_key=True, max_length=20)  # Field name made lowercase.
    ten_hang_sua = models.CharField(db_column='Ten_hang_sua', max_length=100)  # Field name made lowercase.
    dia_chi = models.CharField(db_column='Dia_chi', max_length=200)  # Field name made lowercase.
    dien_thoai = models.CharField(db_column='Dien_thoai', max_length=20)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hang_sua'


class HoaDon(models.Model):
    so_hoa_don = models.CharField(db_column='So_hoa_don', primary_key=True, max_length=5)  # Field name made lowercase.
    ngay_hd = models.DateField(db_column='Ngay_HD')  # Field name made lowercase.
    ma_khach_hang = models.ForeignKey('KhachHang', models.DO_NOTHING, db_column='Ma_khach_hang')  # Field name made lowercase.
    tri_gia = models.FloatField(db_column='Tri_gia')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hoa_don'


class KhachHang(models.Model):
    ma_khach_hang = models.CharField(db_column='Ma_khach_hang', primary_key=True, max_length=5)  # Field name made lowercase.
    ten_khach_hang = models.CharField(db_column='Ten_khach_hang', max_length=100)  # Field name made lowercase.
    phai = models.IntegerField(db_column='Phai')  # Field name made lowercase.
    dia_chi = models.CharField(db_column='Dia_chi', max_length=200)  # Field name made lowercase.
    dien_thoai = models.CharField(db_column='Dien_thoai', max_length=20)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'khach_hang'


class LoaiSua(models.Model):
    ma_loai_sua = models.CharField(db_column='Ma_loai_sua', primary_key=True, max_length=3)  # Field name made lowercase.
    ten_loai = models.CharField(db_column='Ten_loai', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'loai_sua'


class Sua(models.Model):
    ma_sua = models.CharField(db_column='Ma_sua', primary_key=True, max_length=6)  # Field name made lowercase.
    ten_sua = models.CharField(db_column='Ten_sua', max_length=100)  # Field name made lowercase.
    ma_hang_sua = models.ForeignKey(HangSua, models.DO_NOTHING, db_column='Ma_hang_sua')  # Field name made lowercase.
    ma_loai_sua = models.ForeignKey(LoaiSua, models.DO_NOTHING, db_column='Ma_loai_sua')  # Field name made lowercase.
    trong_luong = models.IntegerField(db_column='Trong_luong')  # Field name made lowercase.
    don_gia = models.IntegerField(db_column='Don_gia')  # Field name made lowercase.
    tp_dinh_duong = models.TextField(db_column='Tp_dinh_duong')  # Field name made lowercase.
    loi_ich = models.TextField(db_column='Loi_ich')  # Field name made lowercase.
    hinh = models.CharField(db_column='Hinh', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sua'

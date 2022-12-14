# Generated by Django 4.1.2 on 2022-10-13 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qlbansua', '0002_loaisua_sua'),
    ]

    operations = [
        migrations.CreateModel(
            name='HoaDon',
            fields=[
                ('so_hoa_don', models.CharField(db_column='So_hoa_don', max_length=5, primary_key=True, serialize=False)),
                ('ngay_hd', models.DateField(db_column='Ngay_HD')),
                ('tri_gia', models.FloatField(db_column='Tri_gia')),
            ],
            options={
                'db_table': 'hoa_don',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='KhachHang',
            fields=[
                ('ma_khach_hang', models.CharField(db_column='Ma_khach_hang', max_length=5, primary_key=True, serialize=False)),
                ('ten_khach_hang', models.CharField(db_column='Ten_khach_hang', max_length=100)),
                ('phai', models.IntegerField(db_column='Phai')),
                ('dia_chi', models.CharField(db_column='Dia_chi', max_length=200)),
                ('dien_thoai', models.CharField(db_column='Dien_thoai', max_length=20)),
                ('email', models.CharField(db_column='Email', max_length=100)),
            ],
            options={
                'db_table': 'khach_hang',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CtHoadon',
            fields=[
                ('so_hoa_don', models.OneToOneField(db_column='So_hoa_don', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='qlbansua.hoadon')),
                ('so_luong', models.IntegerField(db_column='So_luong')),
                ('don_gia', models.IntegerField(db_column='Don_gia')),
            ],
            options={
                'db_table': 'ct_hoadon',
                'managed': False,
            },
        ),
    ]

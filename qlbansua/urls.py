from django.urls import path
from . import views
urlpatterns = [
    path("trangchu/<int:vt>", views.trangChu, name='main'),
    path("trangchu/<str:id>&<int:vt>", views.dssTheoHsLs, name='trang_chu'),

    path("trangchu/", views.index),
    path("trangsuabanchay/", views.suaBanChay, name='sua_ban_chay'),
    path("trangsuabanchay/<str:maSua>", views.suaBanChay2, name='sua_ban_chay_2'),
    path("trangthemsuamoi", views.themSuaMoi, name='them_sua_moi'),
    path("trangtimkiemsua/", views.timKiemSua, name='tim_kiem_sua'),
    path("trangthemkhachhang", views.themKhachHang, name='them_khach_hang'),
    path("trangthongtinsua/<str:masua>",
         views.thongTinSua, name='thong_tin_sua'),

]

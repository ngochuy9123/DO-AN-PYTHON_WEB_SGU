
from asyncio.windows_events import NULL
from multiprocessing.dummy import Array
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.db.models import Sum
from .models import HangSua, LoaiSua, Sua, CtHoadon, KhachHang
import array as arr
from itertools import chain
# Create your views here.


def tinhSoTrang(slsp, sosp):
    soTrang = sosp/slsp
    if (sosp % slsp != 0):
        soTrang += 1
    return soTrang


def index(request):
    vt = 0
    slsp = 10
    dshs = HangSua.objects.all()
    dsls = LoaiSua.objects.all()
    dss = Sua.objects.all()[vt*slsp:slsp*vt+slsp]
    sosp = Sua.objects.all().count()
    soTrang = tinhSoTrang(slsp, sosp)
    tongSoTrang = ''
    x = range(1, int(soTrang+1))
    for i in x:
        tongSoTrang += str(i)
    return render(request, "qlbansua/trang-chu.html", {
        "dshs": dshs,
        "dsls": dsls,
        "dss": dss,
        "soTrang": soTrang,
        "tongSoTrang": tongSoTrang
    })


def trangChu(request, vt):
    slsp = 10
    dshs = HangSua.objects.all()
    dsls = LoaiSua.objects.all()
    dss = Sua.objects.all()[vt*slsp:slsp*vt+slsp]
    sosp = Sua.objects.all().count()
    soTrang = tinhSoTrang(slsp, sosp)
    tongSoTrang = ''
    x = range(1, int(soTrang+1))
    for i in x:
        tongSoTrang += str(i)
    return render(request, "qlbansua/trang-chu.html", {
        "dshs": dshs,
        "dsls": dsls,
        "dss": dss,
        "soTrang": soTrang,
        "tongSoTrang": tongSoTrang
    })


def dssTheoHsLs(request, id, vt):
    slsp = 10
    dshs = HangSua.objects.all()
    dsls = LoaiSua.objects.all()
    dss = Sua.objects.filter(ma_hang_sua=id)[vt*slsp:slsp*vt+slsp]

    sosp = Sua.objects.filter(ma_hang_sua=id).count()

    if not dss.count():
        dss = Sua.objects.filter(ma_loai_sua=id)[vt*slsp:slsp*vt+slsp]
        sosp = Sua.objects.filter(ma_loai_sua=id).count()

    soTrang = tinhSoTrang(slsp, sosp)
    tongSoTrang = ''
    x = range(1, int(soTrang+1))
    for i in x:
        tongSoTrang += str(i)
    return render(request, "qlbansua/trang-chu.html", {
        "dshs": dshs,
        "dsls": dsls,
        "dss": dss,
        "soTrangHSLS": soTrang,
        "tongSoTrang": tongSoTrang,
        "id": id
    })


def suaBanChay(request):
    sl = 9
    l = CtHoadon.objects.all()
    mydict = dict()
    j = 1
    k = []
    for i in l:
        if i.ma_sua in mydict:
            mydict[i.ma_sua] = mydict[i.ma_sua]+i.so_luong
        else:
            mydict[i.ma_sua] = i.so_luong
    sort = list(sorted(mydict.items(), reverse=True,
                key=lambda x: x[1]).copy())

    for i in sort:
        if j == 10:
            break
        t = str(i)
        k.append(t[19: 25])
        j = j+1
    dss = Sua.objects.filter(ma_sua=k[0])
    for test in range(1, 9):
        s = Sua.objects.filter(ma_sua=k[test])
        dss = dss | s

    return render(request, "qlbansua/trang-sua-ban-chay.html", {
        "dss": dss,
        "sua": dss[0]
    })


def suaBanChay2(request, maSua):
    sl = 9
    l = CtHoadon.objects.all()
    mydict = dict()
    j = 1
    k = []
    # Luu vao hash map
    for i in l:
        if i.ma_sua in mydict:
            mydict[i.ma_sua] = mydict[i.ma_sua]+i.so_luong
        else:
            mydict[i.ma_sua] = i.so_luong
    # sap theo hash map theo key va value voi chieu ngc la giam dan va sx gia tri value,
    sort = list(sorted(mydict.items(), reverse=True,
                key=lambda x: x[1]).copy())

    # lay 9 masua co sluong nhieu nhat va lay bien t la chuoi de mang k cat chuoi t va lay ma sua

    for i in sort:
        if j == 10:
            break
        t = str(i)
        k.append(t[19: 25])
        j = j+1
    dss = Sua.objects.filter(ma_sua=k[0])
    for test in range(1, 9):
        s = Sua.objects.filter(ma_sua=k[test])
        dss = dss | s

    return render(request, "qlbansua/trang-sua-ban-chay.html", {
        "dss": dss,
        "sua": Sua.objects.get(ma_sua=maSua)
    })


def themSuaMoi(request):
    dshs = HangSua.objects.all()
    dsls = LoaiSua.objects.all()

    if (request.method == 'POST'):
        tenSua = request.POST['txtTenSua']
        maSua = request.POST['txtMaSua']
        maHangSua = request.POST['cboHangSua']
        maLoaiSua = request.POST['cboLoaiSua']
        trongLuong = request.POST['txtTrongLuong']
        donGia = request.POST['txtDonGia']
        image = request.POST['txtHinh']
        tpDinhDuong = request.POST['txtTPDinhDuong']
        loiIch = request.POST['txtLoiIch']
        s = Sua(ma_sua=maSua, ten_sua=tenSua, ma_hang_sua_id=maHangSua, ma_loai_sua_id=maLoaiSua,
                trong_luong=trongLuong, don_gia=donGia, tp_dinh_duong=tpDinhDuong,
                loi_ich=loiIch, hinh=image)
        s.save()
        return render(request, "qlbansua/trang-them-sua-moi.html", {
            'dshs': dshs,
            'dsls': dsls,

        })

    return render(request, "qlbansua/trang-them-sua-moi.html", {
        'dshs': dshs,
        'dsls': dsls,

    })


def thongTinSua(request, masua):
    s = Sua.objects.get(ma_sua=masua)
    return render(request, "qlbansua/trang-thong-tin-sua.html", {
        'sua': s,
    })


def timKiemSua(request):
    dshs = HangSua.objects.all()
    dsls = LoaiSua.objects.all()
    if (request.method == 'POST'):
        ls = request.POST['cboLoaiSua']
        hs = request.POST['cboHangSua']
        s = request.POST['txtTenSuaTim']
        sosp = 0
        dss: list[Sua] = Sua.objects.filter(ten_sua__contains=s).filter(
            ma_hang_sua=hs).filter(ma_loai_sua=ls)
        if (hs == 'none'):
            dss: list[Sua] = Sua.objects.filter(
                ma_loai_sua=ls).filter(ten_sua__contains=s)

        elif (ls == 'none'):
            dss: list[Sua] = Sua.objects.filter(
                ma_hang_sua=hs).filter(ten_sua__contains=s)

        elif (hs == 'none' and ls == 'none'):
            dss: list[Sua] = Sua.objects.filter(ten_sua__contains=s)

        # dss: Sua goi y dang sua

        print(len(dss))

        return render(request, "qlbansua/trang-tim-kiem-sua.html", {
            "dshs": dshs,
            "dsls": dsls,
            "dss": dss,
            "sosp": len(dss)
        })
    return render(request, "qlbansua/trang-tim-kiem-sua.html", {
        "dshs": dshs,
        "dsls": dsls,
    })


def themKhachHang(request):

    if (request.method == 'POST'):
        maKh = request.POST['txtMaKH']
        tenKh = request.POST['txtTenKH']
        phain = int(request.POST['rdbPhai'])
        diaChi = request.POST['txtDiaChi']
        dt = request.POST['txtDienThoai']
        email = request.POST['txtEmail']

        print(tenKh)
        kh = KhachHang(ma_khach_hang=maKh, ten_khach_hang=tenKh, phai=phain, dia_chi=diaChi,
                       dien_thoai=dt, email=email)
        kh.save()
        return render(request, "qlbansua/trang-them-khach-hang.html")

    return render(request, "qlbansua/trang-them-khach-hang.html")

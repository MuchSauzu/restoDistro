
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from Dashboard.views import about, tambah_barang, tambah_user, Barang_View, Administrasi_View
from Dashboard.views import *

def cobax (request):
    return HttpResponse('selamat datang')

def cobay (request):
    titelnya="Home"
    konteks = {
        'titel':titelnya,
    }
    return render(request, 'home.html',konteks)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cobay),
    path('about/', about),
    path('addbrg/', tambah_barang),
    path('Vbrg/', Barang_View),
    path('Vusr/', Administrasi_View),
    path('addusr/', tambah_user),
    path('ubah/<int:id_barang>',ubah_brg,name='ubah_brg'),
    path('hapus/<int:id_barang>',hapus_brg,name="hapus_brg"),
    path('ubahusr/<int:id_administrasi>',ubah_usr,name='ubah_usr'),
    path('hapususr/<int:id_administrasi>',hapus_usr,name="hapus_usr"),
    path('Vmenu/', Menu_View),
    path('Vperson/', Person_View),
]

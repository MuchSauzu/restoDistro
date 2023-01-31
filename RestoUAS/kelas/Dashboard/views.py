from django.shortcuts import render 
from django.shortcuts import redirect
from Dashboard.forms import FormBarang, FormUser
from Dashboard.models import Barang, Administrasi
from django.contrib import messages

# User.
def hapus_usr(request,id_administrasi):
    Administrasis=Administrasi.objects.filter(id=id_administrasi)
    Administrasis.delete()
    messages.success(request,"Data Terhapus")
    return redirect('/Vusr')
    
def ubah_usr(request,id_administrasi):
    Administrasis=Administrasi.objects.get(id=id_administrasi)
    if request.POST:
        form=FormUser(request.POST,instance=Administrasis)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil Diubah")
            return redirect('ubah_usr',id_administrasi=id_administrasi)
    else:
        form=FormUser(instance=Administrasis)
        konteks={
            'form':form,
            'administrasis':Administrasis
        }
    return render(request, 'ubah_user.html',konteks)

def tambah_user(request):
    if request.POST:
        form= FormUser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil Ditambahkan")
            form = FormUser()
            konteks = {
                'form': form,
            }
            return render(request,'tambah_user.html',konteks)
    else:
        form=FormUser()
        konteks={
            'form':form,
        }
    return render(request, 'tambah_user.html',konteks)

def Administrasi_View(request):
    Administrasis=Administrasi.objects.all()
    titelnya="User"
    
    konteks={
        'Administrasis':Administrasis,
        'titel':titelnya,
    }
    return render(request,'tampil_user.html',konteks)

# Barang.
def hapus_brg(request,id_barang):
    barangs=Barang.objects.filter(id=id_barang)
    barangs.delete()
    messages.success(request,"Data Terhapus")
    return redirect('/Vbrg')
    
def ubah_brg(request,id_barang):
    barangs=Barang.objects.get(id=id_barang)
    if request.POST:
        form=FormBarang(request.POST,instance=barangs)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil Diubah")
            return redirect('ubah_brg',id_barang=id_barang)
    else:
        form=FormBarang(instance=barangs)
        konteks={
            'form':form,
            'barangs':barangs
        }
    return render(request, 'ubah_barang.html',konteks)

def Barang_View(request):
    barangs=Barang.objects.all()
    titelnya="Barang"

    konteks={
        'barangs':barangs,
        'titel':titelnya,
    }
    return render(request,'tampil_brg.html',konteks)

def tambah_barang(request):
    if request.POST:
        form= FormBarang(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil Ditambahkan")
            form = FormBarang()
            konteks = {
                'form': form,
            }
            return render(request,'tambah_barang.html',konteks)
    else:
        form=FormBarang()
        konteks={
            'form':form,
        }
    return render(request, 'tambah_barang.html',konteks)

def about(request):
    titelnya="about"
    konteks = {
        'titel':titelnya,
    }
    return render (request,'about.html',konteks)

# Menu dan User

def Person_View(request):
    Administrasis=Administrasi.objects.all()
    titelnya="User"
    
    konteks={
        'Administrasis':Administrasis,
        'titel':titelnya,
    }
    return render(request,'person.html',konteks)

def Menu_View(request):
    barangs=Barang.objects.all()
    titelnya="Menu"

    konteks={
        'barangs':barangs,
        'titel':titelnya,
    }
    return render(request,'menu.html',konteks)
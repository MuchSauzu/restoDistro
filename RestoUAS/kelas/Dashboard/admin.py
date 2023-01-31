from django.contrib import admin

# Register your models here.
from .models import Barang, Jenis, Administrasi

class kolomBarang(admin.ModelAdmin):
    list_display=['kodebrg','nama', 'stok', 'harga', 'jenis_id']
    search_fields=['kodebrg','nama']
    list_filter=['jenis_id']
    list_per_page=3

class kolomUser(admin.ModelAdmin):
    list_display=['userid','nama','usia','lama']
    search_fields=['userid','nama']

admin.site.register(Barang,kolomBarang)
admin.site.register(Jenis)
admin.site.register(Administrasi,kolomUser)
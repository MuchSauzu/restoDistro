from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Jenis(models.Model):
    nama=models.CharField(max_length=50)
    ket=models.TextField()

    def __str__(self):
        return self.nama
class Administrasi(models.Model):
    userid=models.CharField(max_length=10)
    nama=models.CharField(max_length=50)
    usia=models.IntegerField()
    lama=models.IntegerField()
    link_foto=models.CharField(max_length=150, blank=True)

    def __str__(self):
        return "{}, {}".format (self.nama, self.lama)

class Barang(models.Model):
    kodebrg=models.CharField(max_length=8)
    nama=models.CharField(max_length=50)
    stok=models.IntegerField()
    harga=models.BigIntegerField()
    link_gbr=models.CharField(max_length=150, blank=True)
    waktu_posting=models.DateTimeField(auto_now_add=True)
    jenis_id=models.ForeignKey(Jenis, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return "{}, {}, {}".format (self.nama, self.stok, self.harga)
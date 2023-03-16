from LatOOP3 import Manusia

class Mahasiswa(Manusia):
    """Class Mahasiswa yang dibangun dari class Manusia."""

    def __init__(self,nama,NIM,kota,us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia."""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
        self.listKuliah = [] # Tambahan no 4
    def __str__(self):
        s = self.nama + ', NIM ' + str(self.NIM) \
            + '. Tinggal di ' + self.kotaTinggal \
            + '. Uang saku Rp ' + str(self.uangSaku) \
            + ' tiap bulannya.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self,s):
        """Metode ini menutupi metode 'makan'-nya class Manusia.
        Mahasiswa kalau makan sambil belajar."""
        print('Saya baru saja makan',s,'sambil belajar.')
        self.keadaan = 'kenyang'
#Tambahan no 2
    def ambilKotaTinggal(self):
        return self.kotaTinggal
    def perbaruiKotaTinggal(self, kota):
        self.kotaTinggal = kota
    def tambahUangSaku(self, us2):
        self.uangSaku += us2
# Tambahan no 3
nama = input('Masukkan nama : ')
NIM = input('Masukkan NIM : ')
kota = input('Masukkan kota tinggal : ')
us = int(input('Masukkan uang saku : '))

m = Mahasiswa(nama, NIM, kota, us)
print(m)

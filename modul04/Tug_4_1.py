from Lat_4_2 import Daftar;

def cari_mahasiswa(kota):
    hasil_cari = []
    for i in range(len(Daftar)):
        if Daftar[i].kotaTinggal == kota:
            hasil_cari.append(i)
    return hasil_cari

## Output
print(cari_mahasiswa('Klaten'))
print(cari_mahasiswa('Solo'))
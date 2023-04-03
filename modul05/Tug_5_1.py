from Lat_4_2 import Daftar
n = len(Daftar)
for i in range(n):
    for j in range(0, n-i-1):
        if Daftar[j].ambilNIM() > Daftar[j+1].ambilNIM():
            Daftar[j], Daftar[j+1] = Daftar[j+1], Daftar[j]

# Tampilkan daftar Mahasiswa yang sudah terurut
for mhs in Daftar:
    print(mhs)
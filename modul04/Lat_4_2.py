from LatOOP5 import MhsTIF

c0 = MhsTIF('Ika',10,'Sukoharjo', 240000)
c1 = MhsTIF('Budi',51,'Sragen', 235000)
c2 = MhsTIF('Ahmad',2,'Surakarta', 250000)
c3 = MhsTIF('Chandra',18,'Surakarta', 235000)
c4 = MhsTIF('Eka',4,'Boyolali', 240000)
c5 = MhsTIF('Fandi',31,'Salatiga', 250000)
c6 = MhsTIF('Deni',13,'Klaten', 245000)
c7 = MhsTIF('Galuh',5,'Wonogiri', 245000)
c8 = MhsTIF('Janto',23,'Klaten', 245000)
c9 = MhsTIF('Hasan',64,'Karanganyar', 270000)
c10 = MhsTIF('Khalid',29,'Purwodadi', 265000)
##
## Lalu kita membuat daftar mahasiswa dalam bentuk list seperti ini:
##
Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]
target = 'Klaten'
for i in Daftar:
    if i.kotaTinggal == target:
        print(i.nama + ' tinggal di ' + target)


def cariTerkecil(kumpulan):
    n = len(kumpulan)
    # Anggap item pertama adalah yang terkecil
    terkecil = kumpulan[0]
    # tentukan apakah item lain lebih kecil
    for i in range(1, n):
       if kumpulan[i].uangSaku < terkecil.uangSaku: # agar berfungsi 
            terkecil = kumpulan[i]
    return terkecil     # kembalikan yang terkecil


def cari_terkecil():
    n = len(Daftar)
    list = Daftar[0]
    for i in range(n):
        if Daftar[i].uangSaku < list.uangSaku:
            list = Daftar[i]
    print(f'Mahasiswa yang memiliki uang saku terkecil : {list.nama} ({list.uangSaku})')

def cari_terbesar():
    n = len(Daftar)
    list = Daftar[0]
    for i in range(n):
        if Daftar[i].uangSaku > list.uangSaku:
            list = Daftar[i]
    print(f'Mahasiswa yang memiliki uang saku terbesar : {list.nama} ({list.uangSaku})')

def cari_Kurang():
    n = len(Daftar)
    list = []
    for i in range(n):
        if Daftar[i].uangSaku < 250000:
            list.append(Daftar[i])
    for mhs in list:
        print(mhs.nama, end='. ')
    print()

def cari_lebih():
    n = len(Daftar)
    list = []
    for i in range(n):
        if Daftar[i].uangSaku > 250000:
            list.append(Daftar[i])
    for mhs in list:
        print(mhs.nama, end=', ')
    print()


# Output
cari_terkecil()
cari_terbesar()
print('Mahasiswa yang memiliki uang saku kurang dari 250 ribu : ')
cari_Kurang()
print('Mahasiswa yang memiliki uang saku lebih dari 250 ribu : ')
cari_lebih()
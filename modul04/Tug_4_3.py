from Lat_4_2 import Daftar;
from Tug_4_2 import uang_terkecil;

def mhs_uang_terkecil():
    uang_terkecil_value = uang_terkecil()
    mhs = []
    for i in Daftar:
        if i.uangSaku == uang_terkecil_value:
            mhs.append(i)
    return mhs


## output
for m in mhs_uang_terkecil():
    print(m.nama)
from Lat_4_2 import Daftar;

def uang_terkecil():
    uang_saku = []
    for i in Daftar:
        uang_saku.append(i.uangSaku)
    return min(uang_saku)


## output
uang_terkecil()
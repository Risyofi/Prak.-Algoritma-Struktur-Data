from Lat_4_2 import Daftar;

def uang_saku_kurang():
    mhs = []
    for i in Daftar:
        if i.uangSaku < 250000:
            mhs.append(i)
    return mhs


## Output
for m in uang_saku_kurang():
    print(m.nama)
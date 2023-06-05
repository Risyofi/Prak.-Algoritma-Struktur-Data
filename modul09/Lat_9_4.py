from class_SimpulPohonBiner import _SimpulPohonBiner

# Membuat simpul-simpul dan mengisi data
a = _SimpulPohonBiner('Ambarawa')
b = _SimpulPohonBiner('Bantul')
c = _SimpulPohonBiner('Cimahi')
d = _SimpulPohonBiner('Denpasar')
e = _SimpulPohonBiner('Enrekang')
f = _SimpulPohonBiner('Flores')
g = _SimpulPohonBiner('Garut')
h = _SimpulPohonBiner('Halmahera Timur')
i = _SimpulPohonBiner('Indramayu')
j = _SimpulPohonBiner('Jakarta')

# Menghubungkan simpul ortu-anakk
a.kiri = b; a.kanan = c
b.kiri = d; b.kanan = e
c.kiri = f; c.kanan = g
e.kiri = h
g.kanan = i


# b
print("pohon biner b")
a.kiri = b; a.kanan = c
b.kiri = d; b.kanan = e
e.kiri = g
g.kanan = h
h.kiri = i
c.kanan = f

# c
print("pohon biner c")
a.kanan = b
b.kanan = c
c.kiri = d
d.kanan = e
e.kiri = f
f.kanan g
g.kiri = h

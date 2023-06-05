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

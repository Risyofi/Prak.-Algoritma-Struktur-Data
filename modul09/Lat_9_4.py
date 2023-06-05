from class_SimpulPohonBiner import _SimpulPohonBiner, preorderTrav, inorderTrav, postorderTrav

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
print("pohon biner a")
a.kiri = b; a.kanan = c
b.kiri = d; b.kanan = e
c.kiri = f; c.kanan = g
e.kiri = h
g.kiri = i; g.kanan = j

print("preorderTrav : ")
preorderTrav(a)
print("\ninorderTrav : ")
inorderTrav(a)
print("\npostorderTrav : ")
postorderTrav(a)

# b
print("\npohon biner b")
a.kiri = b; a.kanan = c
b.kiri = d; b.kanan = e
c.kanan = f
e.kiri = g
g.kanan = h
h.kiri = i


print("preorderTrav : ")
preorderTrav(a)
print("\ninorderTrav : ")
inorderTrav(a)
print("\npostorderTrav : ")
postorderTrav(a)

# c
print("\npohon biner c")
a.kanan = b
b.kanan = c
c.kiri = d
d.kanan = e
e.kiri = f
f.kanan = g
g.kiri = h

print("preorderTrav : ")
preorderTrav(a)
print("\ninorderTrav : ")
inorderTrav(a)
print("\npostorderTrav : ")
postorderTrav(a)

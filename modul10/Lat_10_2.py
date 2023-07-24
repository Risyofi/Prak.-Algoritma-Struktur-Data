import time

## cara pertama
def jumlahkan_cara_1(n):
    hasilnya = 0
    for i in range(1, n + 1):
        hasilnya = hasilnya + i
    return hasilnya

print("cara pertama")
for i in range(5):
    awal = time.time()
    h = jumlahkan_cara_1(10000)
    akhir = time.time()
    print("Jumlah adalah %d, memerlukan %9.8f detik" % (h, akhir-awal))
print()
    
for i in range(5):
    awal = time.time()
    h = jumlahkan_cara_1(1000000)
    akhir = time.time()
    print("Jumlah adalah %d, memerlukan %9.8f detik" % (h, akhir-awal))
print()

## cara kedua
def jumlahkan_cara_2(n):
    return (n*(n + 1))/2

print("cara kedua")
for i in range(5):
    awal = time.time()
    h = jumlahkan_cara_2(10000)
    akhir = time.time()
    print("Jumlah adalah %d, memerlukan %9.8f detik" % (h, akhir-awal))
print()
    
for i in range(5):
    awal = time.time()
    h = jumlahkan_cara_2(1000000)
    akhir = time.time()
    print("Jumlah adalah %d, memerlukan %9.8f detik" % (h, akhir-awal))
import time

## (a) jumlahkan_cara_1
print('(a) jumlahkan_cara_1')
def jumlahkan_cara_1(n):
    hasilnya = 0
    for i in range(1, n + 1):
        hasilnya = hasilnya + i
    return hasilnya

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

## (b) jumlahkan_cara_2
print('(b) jumlahkan_cara_2')
def jumlahkan_cara_2(n):
    return (n*(n + 1))/2

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
print()

## (c) insertionSort
print('(c) insertionSort')

from insertionSort import insertionSort
import random

## average case scenario
print("average case scenario")
for i in range(5):
    L = list(range(3000))
    random.shuffle(L)
    awal = time.time()
    U = insertionSort(L)
    akhir = time.time()
    print("Mengurutkan %d bilangan, memerlukan %8.7f detik" % (len(L), akhir-awal))
print()

## worst case scenario
print("worst case scenario")
for i in range(5):
    L = list(range(3000))
    L = L[::-1]
    awal = time.time()
    U = insertionSort(L)
    akhir = time.time()
    print("Mengurutkan %d bilangan, memerlukan %8.7f detik" % (len(L), akhir-awal))
print()

## best case scenario
print("best case scenario")
for i in range(5):
    L = list(range(3000))
    awal = time.time()
    U = insertionSort(L)
    akhir = time.time()
    print("Mengurutkan %d bilangan, memerlukan %8.7f detik" % (len(L), akhir-awal))

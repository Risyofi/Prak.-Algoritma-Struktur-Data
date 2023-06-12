from insertionSort import insertionSort
import random
import time

for i in range(5):
    L = list(range(3000))
    random.shuffle(L)
    awal = time.time()
    U = insertionSort(L)
    akhir = time.time()
    print("Mengurutkan %d bilangan, memerlukan %8.7f detik" % (len(L), akhir-awal))
print()

for i in range(5):
    L = list(range(3000))
    L = L[::-1]
    awal = time.time()
    U = insertionSort(L)
    akhir = time.time()
    print("Mengurutkan %d bilangan, memerlukan %8.7f detik" % (len(L), akhir-awal))
print()

for i in range(5):
    L = list(range(3000))
    awal = time.time()
    U = insertionSort(L)
    akhir = time.time()
    print("Mengurutkan %d bilangan, memerlukan %8.7f detik" % (len(L), akhir-awal))
print()

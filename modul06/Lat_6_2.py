from Lat_4_2 import Daftar

def mergeSort(A):
    if len(A) > 1:
        mid = len(A) // 2
        separuhKiri = A[:mid]
        separuhKanan = A[mid:]

        mergeSort(separuhKiri)
        mergeSort(separuhKanan)

        i = 0
        j = 0
        k = 0

        while i < len(separuhKiri) and j < len(separuhKanan):
            if separuhKiri[i].NIM < separuhKanan[j].NIM:
                A[k] = separuhKiri[i]
                i += 1
            else:
                A[k] = separuhKanan[j]
                j += 1
            k += 1

        while i < len(separuhKiri):
            A[k] = separuhKiri[i]
            i += 1
            k += 1

        while j < len(separuhKanan):
            A[k] = separuhKanan[j]
            j += 1
            k += 1

## Output
print('==== mergerSort by NIM ====')
mergeSort(Daftar)
for mhs in Daftar:
    print(mhs.nama, mhs.NIM, mhs.kotaTinggal, mhs.uangSaku)


def quickSort(A):
    quickSortBantu(A, 0, len(A) - 1)


def quickSortBantu(A, awal, akhir):
    if awal < akhir:
        titikBelah = partisi(A, awal, akhir)
        quickSortBantu(A, awal, titikBelah - 1)
        quickSortBantu(A, titikBelah + 1, akhir)

def partisi(A, awal, akhir):
    nilaiPivot = A[awal].NIM
    penandaKiri = awal + 1
    penandaKanan = akhir

    selesai = False
    while not selesai:
        while penandaKiri <= penandaKanan and A[penandaKiri].NIM <= nilaiPivot:
            penandaKiri = penandaKiri + 1

        while A[penandaKanan].NIM >= nilaiPivot and penandaKanan >= penandaKiri:
            penandaKanan = penandaKanan - 1
        
        if penandaKanan < penandaKiri:
            selesai = True
        else:
            temp = A[penandaKiri]
            A[penandaKiri] = A[penandaKanan]
            A[penandaKanan] = temp

    temp = A[awal]
    A[awal] = A[penandaKanan]
    A[penandaKanan] = temp 

    return penandaKanan

## Output
print('\n==== quickSort by NIM ====')
quickSort(Daftar)
for mhs in Daftar:
    print(mhs.nama, mhs.NIM, mhs.kotaTinggal, mhs.uangSaku)


def mergeSortNew(A):
    mergeSortBantu(A, 0, len(A)-1)

def mergeSortBantu(A, awal, akhir):
    if awal < akhir:
        mid = (awal + akhir) // 2
        mergeSortBantu(A, awal, mid)
        mergeSortBantu(A, mid+1, akhir)
        merge(A, awal, mid, akhir)

def merge(A, awal, mid, akhir):
    separuhKiri = mid - awal + 1
    separuhKanan = akhir - mid

    L = [None] * separuhKiri
    R = [None] * separuhKanan

    for i in range(separuhKiri):
        L[i] = A[awal + i]

    for j in range(separuhKanan):
        R[j] = A[mid + 1 + j]

    i = 0
    j = 0
    k = awal

    while i < separuhKiri and j < separuhKanan:
        if L[i].NIM <= R[j].NIM:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    while i < separuhKiri:
        A[k] = L[i]
        i += 1
        k += 1

    while j < separuhKanan:
        A[k] = R[j]
        j += 1
        k += 1
'''
print('==== mergerSort V2 by NIM ====')
mergeSort(Daftar)
for mhs in Daftar:
    print(mhs.nama, mhs.NIM, mhs.kotaTinggal, mhs.uangSaku)
'''

def quickSortNew(A):
    quickSortBantu(A, 0, len(A) - 1)

def quickSortBantu(A, awal, akhir):
    if awal < akhir:
        # Pilih pivot menggunakan metode median-of-three
        pivot = medianOfThree(A, awal, akhir)
        titikBelah = partisi(A, awal, akhir, pivot)
        quickSortBantu(A, awal, titikBelah - 1)
        quickSortBantu(A, titikBelah + 1, akhir)

def partisi(A, awal, akhir, pivot):
    # Cari indeks pivot dalam list
    indeksPivot = A.index(pivot)

    # Tukar elemen pivot ke akhir list
    A[indeksPivot], A[akhir] = A[akhir], A[indeksPivot]

    nilaiPivot = pivot.NIM
    penandaKiri = awal
    penandaKanan = akhir - 1

    selesai = False
    while not selesai:
        while penandaKiri <= penandaKanan and A[penandaKiri].NIM <= nilaiPivot:
            penandaKiri = penandaKiri + 1

        while A[penandaKanan].NIM >= nilaiPivot and penandaKanan >= penandaKiri:
            penandaKanan = penandaKanan - 1
        
        if penandaKanan < penandaKiri:
            selesai = True
        else:
            temp = A[penandaKiri]
            A[penandaKiri] = A[penandaKanan]
            A[penandaKanan] = temp

    # Tukar elemen pivot ke tempat yang tepat
    temp = A[akhir]
    A[akhir] = A[penandaKiri]
    A[penandaKiri] = temp 

    return penandaKiri

def medianOfThree(A, awal, akhir):
    # Cari indeks elemen tengah
    mid = (awal + akhir) // 2

    # Sort elemen awal, tengah, dan akhir
    if A[awal].NIM > A[mid].NIM:
        A[awal], A[mid] = A[mid], A[awal]

    if A[awal].NIM > A[akhir].NIM:
        A[awal], A[akhir] = A[akhir], A[awal]

    if A[mid].NIM > A[akhir].NIM:
        A[mid], A[akhir] = A[akhir], A[mid]

    # Kembalikan elemen tengah sebagai pivot
    return A[mid]

'''
print('\n==== quickSort by NIM ====')
quickSortNew(Daftar)
for mhs in Daftar:
    print(mhs.nama, mhs.NIM, mhs.kotaTinggal, mhs.uangSaku)
'''


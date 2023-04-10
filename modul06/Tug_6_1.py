from Lat_4_2 import Daftar

def mergeSort(A):
    #print('Membelah      ', A)
    if len(A) > 1:
        mid = len(A) // 2
        separuhKiri = A[:mid]
        separuhKanan = A[mid:]

        mergeSort(separuhKiri)
        mergeSort(separuhKanan)

        # Dibawah ini adalah proses penggabungan.
        i = 0; j = 0; k = 0
        while i < len(separuhKiri) and j < len(separuhKanan):
            if separuhKiri[i] < separuhKanan[j]:
                A[k] = separuhKiri[i]
                i = i + 1
            else:
                A[k] = separuhKanan[j]
                j = j + 1
            k = k + 1

        while i < len(separuhKiri):
            A[k] = separuhKiri[i]
            i = i + 1
            k = k + 1

        while j < len(separuhKanan):
            A[k] = separuhKanan[j]
            j = j + 1
            k = k + 1
    #print('Menggabungkan ', A)

def convert(arr, object):
    result = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] == object[j].NIM:
                result.append(object[j])
    return result

A = []
for i in Daftar:
    A.append(i.NIM)

def print_result():
    for i in convert(A, Daftar):
        print("[", i.nama,i.NIM,i.kotaTinggal,i.uangSaku, "]")


# Output
print('--mergeSort by NIM--')
mergeSort(A)
print_result()

#=================================Quick Sort====================================
def quickSort(A):
    quickSortBantu(A, 0, len(A) - 1)

def quickSortBantu(A, awal, akhir):
    if awal < akhir:
        titikBelah = partisi(A, awal, akhir)
        quickSortBantu(A, awal, titikBelah - 1)
        quickSortBantu(A, titikBelah + 1, akhir)

def partisi(A, awal, akhir):
    nilaiPivot = A[awal]
    penandaKiri = awal + 1
    penandaKanan = akhir

    selesai = False
    while not selesai:
        while penandaKiri <= penandaKanan and A[penandaKiri] <= nilaiPivot:
            penandaKiri = penandaKiri + 1

        while A[penandaKanan] >= nilaiPivot and penandaKanan >= penandaKiri:
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

# Output 
print('\n--quickShort by NIM--')
quickSort(A)
print_result()

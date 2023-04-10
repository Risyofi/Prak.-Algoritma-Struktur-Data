from Lat_4_2 import Daftar


def mergeSort2(A, start, end):
    if start < end:
        mid = (start + end) // 2
        mergeSort2(A, start, mid)
        mergeSort2(A, mid+1, end)
        merge(A, start, mid, end)

def merge(A, start, mid, end):
    temp = [0] * (end - start + 1)
    i = start
    j = mid+1
    k = 0

    while i <= mid and j <= end:
        if A[i] < A[j]:
            temp[k] = A[i]
            i += 1
        else:
            temp[k] = A[j]
            j += 1
        k += 1

    while i <= mid:
        temp[k] = A[i]
        i += 1
        k += 1

    while j <= end:
        temp[k] = A[j]
        j += 1
        k += 1

    for i in range(start, end+1):
        A[i] = temp[i-start]

def mergeSortNew(A):
    mergeSort2(A, 0, len(A)-1)
    
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
#print('--mergeSort by NIM--')
mergeSortNew(A)
#print_result()

def jumlahkan_cara_1(n):
    hasilnya = 0
    for i in range(1, n+1):
        hasilnya = hasilnya + i
    return hasilnya

print(jumlahkan_cara_1(10))
print(jumlahkan_cara_1(100))

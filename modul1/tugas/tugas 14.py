def formatRupiah(x):
    x = str(x)
    panjang = len(x)
    jumlahTitik = (panjang - 1) // 3

    for i in range(jumlahTitik):
        posisiTitik = panjang - (i+1)*3
        x = x[:posisiTitik] + '.' + x[posisiTitik:]
    return "'Rp " + x + "'"

print(formatRupiah(1500))
print(formatRupiah(2560000000))
def binSe(kumpulan, target):
    # Mulai dari seluruh runtutan element
    low = 0
    high = len(kumpulan) - 1
    index = []

    # Secara berulang belah runtutan itu menjadi separuhnya sampai targetnya ditemukan
    while low <= high:
        # Temukan pertengahan runtut itu
        mid = (high + low) // 2
        # Apakah pertengahannya memuat target?
        if kumpulan[mid] == target:
            index.append(mid)
            # cari indexs target yang ada di sebelah kir pertengahan
            i = mid - 1
            while i >= low and kumpulan[i] == target:
                index.append(i)
                i -= 1
            # cari indexs target yang ada di sebelah kanan pertengahan
            i = mid + 1
            while i <= high and kumpulan[i] == target:
                index.append(i)
                i += 1

            return index
        # Ataukah targetnya di sebelah kirinya?
        elif target < kumpulan[mid]:
            high = mid - 1
            # ataukah targetnya di sebelah kanannya?
        else:
            low = mid + 1
    # jika runtutnya tidak bisa dibelah lagi, berarti targetnya tidak ada
    return False

## Output
kumpulan = [2, 3, 5, 6, 6, 6, 8, 9, 9, 10, 11, 12, 13, 13, 14]
print(binSe(kumpulan, 6))
print(binSe(kumpulan, 4))
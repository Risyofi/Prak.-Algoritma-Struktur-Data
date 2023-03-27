def binSe(kumpulan, target):
    # Mulai dari seluruh runtutan element
    low = 0
    high = len(kumpulan) - 1

    # Secara berulang belah runtutan itu menjadi separuhnya sampai targetnya ditemukan
    while low <= high:
        # Temukan pertengahan runtut itu
        mid = (high + low) // 2
        # Apakah pertengahannya memuat target?
        if kumpulan[mid] == target:
            return True
        # Ataukah targetnya di sebelah kirinya?
        elif target < kumpulan[mid]:
            high = mid - 1
            # ataukah targetnya di sebelah kanannya?
        else:
            low = mid + 1
    # jika runtutnya tidak bisa dibelah lagi, berarti targetnya tidak ada
    return False


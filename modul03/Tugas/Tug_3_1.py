def cek_konsistensi(matrix):
    rows = len(matrix)
    cols = len(matrix)
    for i in range(rows):
        if len(matrix[i]) != cols:
            return False
    return True

def ukuran(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    return (rows, cols)

def jumlah(matrix1, matrix2):
    rows1, cols1 = ukuran(matrix1)
    rows2, cols2 = ukuran(matrix2)
    if cols1 != rows2:
        return False
    if not cek_konsistensi(matrix1) or not cek_konsistensi(matrix2):
        return False
    result = []
    for i in range(rows1):
        row = []
        for j in range(cols1):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

def kali(matrix1, matrix2):
    rows1, cols1 = ukuran(matrix1)
    rows2, cols2 = ukuran(matrix2)
    if cols1 != rows2:
        return False
    if not cek_konsistensi(matrix1) or not cek_konsistensi(matrix2):
        return False
    result = []
    for i in range(rows1):
        row = []
        for j in range(cols2):
            total = 0
            for k in range(cols1):
                total += matrix1[i][k] * matrix2[k][j]
            row.append(total)
        result.append(row)
    return result

def determinan(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if cek_konsistensi(matrix) and n == ukuran(matrix)[0]:
        det = 0
        for i in range(n):
            minor = []
            for j in range(1, n):
                minor_row = []
                for k in range(n):
                    if k != i:
                        minor_row.append(matrix[j][k])
                minor.append(minor_row)
            det += ((-1) ** i) * matrix[0][i] * determinan(minor)
        return det
    else:
        return False


## Output
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[1, 2, 3], [4, 5], [6, 7, 9, 8]]
matrix3 = [[9, 8, 7], [4, 'i', 4], [1, 'd']]
matrix4 = [[1, 2], [3, 4]]
matrix5 = [[1, 2], [3, 3]]
## contoh fungsi cek_konsistensi(matrix)
print(cek_konsistensi(matrix1))
print(cek_konsistensi(matrix2))
print(cek_konsistensi(matrix3))
print(cek_konsistensi(matrix4))

## contoh fungsi ukuran(matrix)
print(ukuran(matrix1))
print(ukuran(matrix2))
print(ukuran(matrix3))
print(ukuran(matrix4))

## contoh fungsi jumlah(matrix1, matrix2)
print(jumlah(matrix4, matrix5))
print(jumlah(matrix4, matrix3))
print(jumlah(matrix4, matrix1))
print(jumlah(matrix2, matrix1))

## contoh fungsi kali(matrix1, matarix2)
print(kali(matrix4, matrix5))
print(kali(matrix2, matrix1))

## contoh fungsi determinan(matrix)
print(determinan(matrix1))
print(determinan(matrix2))
print(determinan(matrix3))
print(determinan(matrix4))
print(determinan(matrix5))
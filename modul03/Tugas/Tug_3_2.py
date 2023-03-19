def buatNol(m, n=None):
    if n is None:
        n = m
    return [[0 for j in range(n)] for i in range(m)]

def buatIdentitas(m):
    return [[1 if j == i else 0 for j in range(m)] for i in range(m)]


## contoh fungsi buatNol(m, n=None)
print(buatNol(4, 4))
print(buatNol(3))

## contoh fungsi buatIdentitas(m)
print(buatIdentitas(4))
print(buatIdentitas(3))
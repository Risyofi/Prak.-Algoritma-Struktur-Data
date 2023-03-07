def faktorPrima(x):
    faktor_prima = []
    i = 2
    while i <= x:
        if x % i == 0:
            faktor_prima.append(i)
            x = x / i
        else: 
            i += 1
    return tuple(faktor_prima)

print(faktorPrima(10))
print(faktorPrima(120))
print(faktorPrima(19))
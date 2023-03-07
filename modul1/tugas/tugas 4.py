def rerata(x): 
    total = 0
    for i in range(len(x)):
        total += x[i]
    rata_rata = total / len(x)
    return rata_rata

print(rerata([1,2,3,4,5]))

g = [3,4,5,4,3,4,5,2,2,10,11,23]
print(rerata(g))
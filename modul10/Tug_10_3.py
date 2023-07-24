import matplotlib.pyplot as plt
import timeit
import time
import random

def a(n):
    test = 0
    for i in range(n):
        for j in range(n):
            test = test + i * j

def ujia(n):
    ls = []
    jangkauan = range(1, n+1)
    siap = 'from __main__ import a'
    for i in jangkauan:
        t = timeit.timeit('a(' + str(i) + ')', setup=siap, number=1)
        ls.append(t)
    return ls

n = 10
LS = ujia(n)
plt.plot(LS)
skala = 7700000
plt.plot([x*x/skala for x in range(1, n+1)], 'r')
plt.show()

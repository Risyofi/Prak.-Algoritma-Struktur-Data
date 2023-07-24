import matplotlib.pyplot as plt
import timeit

def loop(n):
    i = n
    while i > 0:
        k = 2 + 2
        i = i // 2

def testing(n):
    ls = []
    coverage = range(1, n+1)
    ready = 'from __main__ import loop'
    for i in coverage:
        t = timeit.timeit('loop(' + str(i) + ')', setup=ready, number=1)
        ls.append(t)
    return ls

n = 10
LS = testing(n)
plt.plot(LS)
skala = 7700000
plt.plot([x*x/skala for x in range(1, n+1)])
plt.show()

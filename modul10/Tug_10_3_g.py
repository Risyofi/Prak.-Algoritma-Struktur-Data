import matplotlib.pyplot as plt
import timeit

def loop(n):
    sum = 0
    for i in range(n):
        if i % 3 == 0:
            for j in range(n//2):
                sum += j
        elif i % 2 == 0:
            for j in range(5):
                sum += j
        else:
            for j in range(n):
                sum += j

def testing(n):
    ls = []
    coverage = range(1, n+1)
    ready = 'from __main__ import loop'
    for i in coverage:
        t = timeit.timeit('loop(' + str(i) + ')', setup=ready, number=1)
        ls.append(t)
    return ls

n = 100
LS = testing(n)
plt.plot(LS)
skala = 7700000
plt.plot([x*x/skala for x in range(1, n+1)])
plt.show()

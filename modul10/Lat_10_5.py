from timeit import timeit

print(timeit('sqrt(2)', 'from math import sqrt', number=10000))
print(timeit('sqrt(2)', 'from math import sqrt', number=100000))
print(timeit('sqrt(2)', 'from math import sqrt', number=1000000))

print(timeit('1+2'))
print(timeit('sin(pi/3)', setup='from math import sin, pi',))
print(timeit('sin(1.047)', setup='from math import sin',))
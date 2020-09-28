"""
ex4.py
formatting exercise from lab 8
created by sands 6/12/10
"""

from math import sqrt, log, log10

start = int(input("Start value: "))
finish = int(input("End value: "))

for n in range(start, finish+1) :
    print("{0:3d} {1:6d} {2:9d} {3:5.2f} {4:8.4f} {5:8.4f}".format(n, n*n,
          n**3, sqrt(n), log(n,2), log10(n)))





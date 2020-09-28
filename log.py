"""
log.py
calculation of logarithms base 2 and 10 of a series of numbers
where start, final and step values are input by the user
"""

from math import log10, log

first = float(input("Please enter initial value for x : "))
last = float(input("final value for x : "))
step = float(input("and step : "))

string = format("x",">6s") + format("log10 x", ">12s") \
          + format("log2 x", ">12s")
print(string)

x = first
while x <= last :
    string = format(x, "6.2f") + format(log10(x), "12.3f")
    string = string + format(log(x,2), "12.3f")
    print(string)
    x = x + step



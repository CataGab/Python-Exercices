"""
squares.py
formatted output of squares and cubes
created by sands 30/10/10
"""

i = 1
line = ""
while i <= 10:
    line = line + format(i, "5d")
    i = i + 1
print(line)

i = 1
line = ""
while i <= 10:
    line = line + format(i * i, "5d")
    i = i + 1
print(line)

i = 1
line = ""
while i <= 10:
    line = line + format(i ** 3, "5d")
    i = i + 1
print(line)

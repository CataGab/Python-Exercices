"""
arith3.py
performs simple calculations on input
created by sands 14/10/10
"""

x = int(input("Enter value for x: "))
y = int(input("Enter value for y: "))

print("twice x is", x+x)
square = x * x
# first attempt used the following code to calculate the cube
# cube = square * x
cube = x ** 3
print("the square of x is", square)
print("the cube of x is", cube)

print("the sum of x and y is", x+y)
print("the product of x and y is", x*y)
print("the difference between x and y is", abs(x-y))





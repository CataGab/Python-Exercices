"""
comp1.py
written by sands 12/10/10
"""

x = int(input("Enter value for x: "))
y = int(input("Enter value for y: "))
z = int(input("Enter value for z: "))

print("x is", x, "and y is", y)
print("x<y is", x<y)
print("x==y is", x==y)
print("x!=y is", x!=y)
print("x<=y is", x<=y)
print("x>=y is", x>=y)
print("x>y is", x>y)

print("The following statement(s) are true:")
if x==y : print("x is equal to y")
if x!=y : print("x is not equal to y")
if x<y : print("x is less than y")
if x>y : print("x is greater than y")

print("In ascending order, the numbers are")
# first version - two numbers in ascending order
# if x<y : print(x, y)
# else : print(y, x)
if x<y : 
    # x comes before y, need to work out where z goes
    if z<x : print(z, x, y)
    elif z>y : print(x, y, z)
    else : print(x, z, y)
else :
    # y comes before x, need to work out where z goes
    if z<y : print(z, y, x)
    elif z>x : print(y, x, z)
    else : print(y, z, x)






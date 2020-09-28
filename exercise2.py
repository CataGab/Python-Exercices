"""
exercise2.py
factorial calculation
created by sands 1/11/10
"""

def factorial(n) :
    """
    calculates factorial of n
    argument: n: int
    returns: n!: int
    """
    result = 1
    i = 2
    while i<=n :
        result = result * i
        i = i+1
    return result

print("Use a negative number to terminate input")

running = True

while running :
    # get number - check if its negative
    myNum = int(input("Enter an integer: "))
    if myNum < 0 : running = False
    else : print(str(myNum)+"! is", factorial(myNum))

"""
ass1.py
CE151 assignment 1 template
created by sands 30/10/10
modified by sands 28/10/11 - number of exercises changed
modified by sands 28/10/6 - number of exercises changed, example added
"""

from math import sqrt

def ex0():
    """
    example
    use 8 at exercise selection prompt in my code to select it
    """
    i = int(input("Enter a non-negative integer: "))
    if i<0:
        print("Negative numbers do not have real square roots")
    else:
        root = sqrt(i)
        print("The square root is", round(root, 2))
        
def ex1() :
    """
    exercise 1
    """
    print("Exercise 1 not attempted")
    
def ex2() :
    """
    exercise 2
    """
    print("Exercise 2 not attempted")
    
def ex3() :
    """
    exercise 3
    """
    print("Exercise 3 not attempted")
    
def ex4() :
    """
    exercise 4
    """
    print("Exercise 4 not attempted")
    
def ex5() :
    """
    exercise 5
    """
    print("Exercise 5 not attempted")
    
def ex6() :
    """
    exercise 6
    """
    print("Exercise 6 not attempted")
    
def ex7() :
    """
    exercise 7
    """
    print("Exercise 7 not attempted")


# modify the following line so that your name is displayed instead of Lisa's
print("CE151 assignment 1 - Lisa Simpson")

# do not modify anything beneath this line
exlist = [None, ex1, ex2, ex3, ex4, ex5, ex6, ex7, ex0]
running = True
while running :
    line = input("Select exercise (0 to quit): ")
    if line == "0" : running = False
    elif len(line)==1 and "1"<=line<="8": exlist[int(line)]()
    else : print("Invalid input - try again")



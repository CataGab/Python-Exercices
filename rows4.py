"""
rows4.py
program to display rectangles of alternating characters
created by sands 29/10/10
"""

def printRow(c, length) :
    """
    print a row of identical characters
    arguments:
    c: str: character to be used
    length: int: length of row
    """
    line = c*length
    print(line)

def printAlternatingRow(c1, c2, length) :
    """
    print a row of alternating characters
    arguments:
    c1, c2: str: characters to be used
    length: int: length of row
    """
    # generate row of form +=+=+=
    line = (c1+c2) * (length//2)
    # if length is odd need to add an extra character to end of row
    if length%2 == 1 : line = line+c1
    print(line)

def printRec(c1, c2, rows, cols) :
    """
    print a rectangle of alternating characters
    arguments :
    c1, c2 : str : characters to be used
    rows : int : number of rows
    cols : int : number of columns
    """
    # use rows to keep track of how many rows are still to be printed
    while rows>0:
        printAlternatingRow(c1, c2, cols)
        rows = rows - 1

myChar1 = input("Select first character: ")
myChar2 = input("Select second character: ")
myRows = int(input("How many rows? "))
myCols = int(input("How many columns? "))

printRec(myChar1[0], myChar2[0], myRows, myCols)



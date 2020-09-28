"""
rows3.py
program to display rectangles of characters
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

def printRec(c, rows, cols) :
    """
    print a rectangle of identical characters
    arguments :
    c : str : character to be used
    rows : int : number of rows
    cols : int : number of columns
    """
    # use rows to keep track of how many rows are still to be printed
    while rows>0:
        printRow(c, cols)
        rows = rows - 1

myChar = input("Select character: ")
myRows = int(input("How many rows? "))
myCols = int(input("How many columns? "))

printRec(myChar[0], myRows, myCols)



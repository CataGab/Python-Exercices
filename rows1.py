"""
rows1.py
program to display rows of characters
created by sands 23/10/10
edited 29/10/10
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

printRow('=', 10)
printRow('*', 7)
myChar = input("Select character: ")
myLen = int(input("Length of row: "))
printRow(myChar[0], myLen)



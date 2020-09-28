"""
rows2.py
program to display triangles of characters
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

myChar = input("Select character: ")
myLen = int(input("Length of first row: "))

# save length - we need it to tell when we've reached the last row
savedLen = myLen

# print upper triangle
while myLen>0:
    printRow(myChar[0], myLen)
    myLen = myLen-1

#print rest of lower triangle
#already have row of length 1 so start at 2
myLen = 2
while myLen<=savedLen:
    printRow(myChar[0], myLen)
    myLen = myLen+1



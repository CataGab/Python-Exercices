"""
rows6.py
program to display rectangle of characters with diamond pattern
created by sands 29/10/10
"""

def printRow(c1, c2, l1, l2) :
    """
    print a row of identical characters:
        l1 copies of c1 then l2 copies of c2 then another l1 copies of c1
    arguments:
    c1, c2: str: characters to be used
    l1, l2: int: lengths of segments of row
    """
    line = c1*l1 + c2*l2 + c1*l1
    print(line)

myChar1 = input("Select first character: ")
myChar2 = input("Select second character: ")
myLen = int(input("Length of first segment"))

# variable for length of middle portion
midLen = 1

# print upper triangle
while myLen>0:
    printRow(myChar1[0], myChar2[0], myLen, midLen)
    myLen = myLen-1
    midLen = midLen+2

#print rest of lower triangle
#already have row of length 1 so start at 2
myLen = 2
#adjust midLen - need 2 less than last value used
#                have added 2 to last value used so need to subtract 4
midLen = midLen-4
#last line has midLen 1 so stop when midLen becomes less than 1
while midLen>=1:
    printRow(myChar1[0], myChar2[0], myLen, midLen)
    myLen = myLen+1
    midLen = midLen-2



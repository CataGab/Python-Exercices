"""
dictcount1.py
counts occurrences of each letter in a line of text and outputs to file
version using dictionary
created by sands 12/11/10
"""

# set up empty dictionary
occs = { }

line  = input("Please input a line of text\n")

for c in line :
    if ord(c)<=127 :  
        if c in occs :
            occs[c] = occs[c]+1
        else :
            occs[c] = 1

fileName = "occs.txt"

f = open(fileName, 'w')
print("Output will be sent to", fileName)

if occs.get(' ')==1 : sp = "space"
else : sp = "spaces"
print("The line contained", occs.get(' ',0), sp, file = f)

for c in occs :
    if ord(c)>32:
        print("The number of occurrences of", c, "was", occs[c], file = f)

f.close()

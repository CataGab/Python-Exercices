"""
dictcount2.py
counts occurrences of each letter in a line of text and outputs to file
version using dictionary and items()
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

for i in occs.items() :
        if ord(i[0])>32:
            print("The number of occurrences of", i[0], "was", i[1], file = f)

f.close()

"""
dictcount3.py
counts occurrences of each letter in a line of text and outputs to file
version using dictionary and items() with sorted output
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

outFile = "occs.txt"

fOut = open(outFile, 'w')
print("Output will be sent to", outFile)

if occs.get(' ')==1 : sp = "space"
else : sp = "spaces"
print("The line contained", occs.get(' ',0), sp, file = fOut)

myItems = list(occs.items())
myItems.sort()
for i in myItems :
    ch, oc = i
    if ord(ch)>32:
        print("The number of occurrences of", ch, "was", oc, file = fOut)

fOut.close()

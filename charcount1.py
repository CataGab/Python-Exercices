"""
charcount1.py
counts occurrences of each letter in a line of text and outputs to file
created by sands 12/11/10
"""

# set up list with 128 ints, all initially 0
occs = [0] * 128

line  = input("Please input a line of text\n")

for c in line :
    if ord(c)<=127 :  
        occs[ord(c)] += 1

outFile = "occs.txt"

fOut = open(outFile, 'w')
print("Output will be sent to", outFile)

if occs[32]==1 : sp = "space"
else : sp = "spaces"
print("The line contained", occs[32], sp, file = fOut)

i = 33
while i<128 :
    if occs[i]!=0 :
        print("The number of occurrences of", chr(i), "was", occs[i], file = fOut)
    i = i+1

fOut.close()

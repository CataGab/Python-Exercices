"""
charcount2.py
counts occurrences of each letter in a line of text and outputs to file
outputs to stdout if file cannot be opened
created by sands 12/11/10
"""

from sys import stdout

# set up list with 128 ints, all initially 0
occs = [0] * 128

line  = input("Please input a line of text\n")

for c in line :
    if ord(c)<=127 :
        occs[ord(c)] += 1

outFile = input("Specify output file: ")

try :
    fOut = open(outFile, 'w')
    print("Output will be sent to", outFile)
except IOError as e :
    fOut = stdout
    print("Failed to open", outFile, "- using standard output instead")
if occs[32]==1 : sp = "space"
else : sp = "spaces"
print("The line contained", occs[32], sp, file = fOut)
i = 33
while i<128 :
    if occs[i]!=0 :
        print("The number of occurrences of", chr(i), "was", occs[i], file = fOut)
    i = i+1

if fOut!=stdout:
    fOut.close()

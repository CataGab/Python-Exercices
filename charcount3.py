"""
charcount3.py
counts occurrences of each letter in a file and outputs to file
outputs to stdout if file cannot be opened
created by sands 12/11/10
"""

from sys import stdout

# set up list with 128 ints, all initially 0
occs = [0] * 128

inFile = input("Specify input file: ")
try :
    fIn = open(inFile)
except IOError as e :
    fIn = None
    print("Failed to open", inFile, "- program aborted")

if fIn != None:
    line = fIn.readline()
    while len(line) > 0 :
        for c in line :
            if ord(c)<=127 :
                occs[ord(c)] += 1
        line = fIn.readline()
    fIn.close()

    outFile = input("Specify output file: ")

    try :
        fOut = open(outFile, 'w')
        print("Output will be sent to", outFile)
    except IOError as e :
        fOut = stdout
        print("Failed to open", outFile, "- using standard output instead")

    if occs[32]==1 : sp = "space"
    else : sp = "spaces"
    if occs[ord('\n')]==1 : nl = "newline"
    else : nl = "newlines"
    print("The file contains", occs[32], sp, "and", occs[ord('\n')], nl, file = fOut)
    i = 33
    while i<128 :
        if occs[i]!=0 :
            print("The number of occurrences of", chr(i), "was", occs[i], file = fOut)
        i = i+1

    if fOut!=stdout:
        fOut.close()
        


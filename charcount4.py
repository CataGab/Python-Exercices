"""
charcount4.py
counts occurrences of each letter in a file and appends it to file
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
    for line in fIn :
        for c in line :
            if ord(c)<=127 :
                occs[ord(c)] += 1
    fIn.close()

    outFile = input("Specify output file: ")

    try :
        fOut = open(outFile, 'a')
        print("Output will be appended to", outFile)
    except IOError as e :
        fOut = stdout
        print("Failed to open", outFile, "- using standard output instead")

    fOut.write("\n"+inFile+"\n\n")

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
        


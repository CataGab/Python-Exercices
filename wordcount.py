"""
wordcount.py
counts occurrences of each word in a file and outputs to screen
created by sands 29/11/10
"""

# set up empty dictionary
occs = { }

fileName = input("Please supply name of input file: ")
gotIt = False
try :
    f = open(fileName)
    gotIt = True
except IOError as e :
    print("Failed to open", fileName)
    
if gotIt :
    for line in f :
        words = line.lower().split()
        for word in words:  
            if word in occs :
                occs[word] = occs[word]+1
            else :
                occs[word] = 1

    f.close()

    for i in occs.items() :
        word, oc = i
        print("The number of occurrences of", word.capitalize(), "was", oc)


"""
xhtml2.py
checks nesting of tags in XHTML
handles multiple-line tags
reports line numbers
written by sands 30/11/2010
"""

def checkNesting(l) :
    """
    checks if tags are correctly nested
    argument: l: list of (int,str) tuples
    returns result : boolean , True if nesting is correct, False otherwise
    outputs error message if incorrect
    """

    myStack = []

    for tup in l :
        lineNum, tag = tup
        if tag[1]!='/' :
            # opening tag
            if tag[-2] != '/' :
                # not self-closing so get name and add it to stack 
                i = 1
                while tag[i]!=' ' and tag[i]!='>' and tag[i]!='\n' :
                    i = i+1
                name = tag[1:i]
                myStack.append((lineNum, name))
        else :
            # get name
            i = 2
            while tag[i]!=' ' and tag[i]!='>' and tag[i]!='\n' :
                i = i+1
            name = tag[2:i]
            # if stack is empty :
            if myStack == [] :
                # output error message - no matching opening brack for c
                print("Error - no matching opening tag for", tag, "on line", lineNum)
                return False
            else :
                # pop top item from stack
                topNum, topName = myStack.pop()
                # if it doesn't match name
                if topName != name :
                    # output error message - expected match for top item, got c
                    print("Error - expected match for", '<'+topName+'>', "on line", topNum,
                          "got", tag, "on line", lineNum)
                    return False


    # if stack is not empty :
    if myStack != [] :
        # output error message - match for top item on stack missing
        print("Error - match for", '<'+myStack[-1][1]+'>', "on line", myStack[-1][0], "missing")
        return False
    else :
        return True

fileName = input("Specify name of HTML file: ")
f = open(fileName)

tags = []

lineNum = 0
line = f.readline()
savedLine = None
while len(line)!=0 :
    lineNum = lineNum + 1
    if savedLine != None :
        line = savedLine + line
        savedLine = None
    searching = True
    while searching :
        start = end = None
        length = len(line)
        i = 0
        while i<length and line[i] != '<' :
            i = i+1
        if i<length :
            start = i
            while i<length and line[i] != '>' :
                i = i+1
            if i<length :
                end = i
            else : 
                savedLine = line
                searching = False
        if start == None :
            searching = False
        elif end != None :
            slice = line[start:end+1]
            tags.append((lineNum, slice))
            line = line[end+1:]
    line = f.readline()

f.close()

# print(tags)
if checkNesting(tags) : print("Succesfully checked")


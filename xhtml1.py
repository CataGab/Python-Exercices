"""
xhtml1.py
checks nesting of tags in XHTML
does not handle multiple-line tags
written by sands 30/11/2010
"""

def checkNesting(l) :
    """
    checks if tags are correctly nested
    argument: l: list of str
    returns result : boolean , True if nesting is correct, False otherwise
    outputs error message if incorrect
    """

    myStack = []

    for tag in l :
        if tag[1]!='/' :
            # opening tag
            if tag[-2] != '/' :
                # not self-closing so get name and add it to stack 
                i = 1
                while tag[i]!=' ' and tag[i]!='>' :
                    i = i+1
                name = tag[1:i]
                myStack.append(name)
        else :
            # get name
            i = 2
            while tag[i]!=' ' and tag[i]!='>' :
                i = i+1
            name = tag[2:i]
            # if stack is empty :
            if myStack == [] :
                # output error message - no matching opening brack for c
                print("Error - no matching opening tag for", tag)
                return False
            else :
                # pop top item from stack
                top = myStack.pop()
                # if it doesn't match name
                if top != name :
                    # output error message - expected match for top item, got c
                    print("Error - expected match for", '<'+top+'>', "got", tag)
                    return False


    # if stack is not empty :
    if myStack != [] :
        # output error message - match for top item on stack missing
        print("Error - match for", '<'+myStack[-1]+'>', "missing")
        return False
    else :
        return True

fileName = input("Specify name of HTML file: ")
f = open(fileName)

tags = []

line = f.readline()
while len(line)!=0 :
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
        if end == None :
            searching = False
        else :
            slice = line[start:end+1]
            tags.append(slice)
            line = line[end+1:]
    line = f.readline()

f.close()

# print(tags)
if checkNesting(tags) : print("Succesfully checked")


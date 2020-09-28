"""
nest1.py
Brackets, braces and parenthesis test
"""
def checkNesting(s) :
    """
    checks if brackets, braces and parenthesis in expression s
    are correctly nested
    argument: s : str
    returns result : boolean , True if nesting is correct, False otherwise
    outputs error message if incorrect
    outline written by sands 7/11/10
    final version written by rturnr/sands 15/11/10
    """

    myStack = []

    i = 0
    while i < len(s) :
        if s[i] in "{[(" :
            # push c onto stack
            myStack.append(s[i])

        elif s[i] in "}])" :
            # assign to c1 the opening brack that corresponds to s[i]
            if s[i]  == '}' : c1 = '{'
            elif s[i] == ']' : c1 = '['
            else :  c1 = '('
            # if stack is empty :
            if myStack == [] :
                # output error message - no matching opening brack for s[i]
                print("Error - no matching opening brack", c1, "for", s[i])
                return False
            else :
                # pop top item from stack
                top = myStack.pop()
                # if it doesn't match s[i]
                if top != c1 :
                    # output error message - expected match for top item, got s[i]
                    print("Error - expected match for", top, "got", s[i])
                    return False
        i = i+1


    # if stack is not empty :
    if myStack != [] :
        # output error message - match for top item on stack missing
        print("Error - match for top item on stack", myStack[-1], "missing")
        return False
    else :
        return True

s = input("Please enter an expression : ")
if  checkNesting(s) : print("Expression correctly formed")

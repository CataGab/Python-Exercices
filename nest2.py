"""
nest2.py
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
    final version written by rturnr 15/11/10
    """

    myStack = []

    for c in s :
        if c in "{[(" :
            # push c onto stack
            myStack.append(c)

        elif c in "}])" :
            # assign to c1 the opening brack that corresponds to c
            if c  == '}' : c1 = '{'
            elif c == ']' : c1 = '['
            else :  c1 = '('
            # if stack is empty :
            if myStack == [] :
                # output error message - no matching opening brack for c
                print("Error - no matching opening brack", c1, "for", c)
                return False
            else :
                # pop top item from stack
                top = myStack.pop()
                # if it doesn't match c
                if top != c1 :
                    # output error message - expected match for top item, got c
                    print("Error - expected match for", top, "got", c)
                    return False


    # if stack is not empty :
    if myStack != [] :
        # output error message - match for top item on stack missing
        print("Error - match for top item on stack", myStack[-1], "missing")
        return False
    else :
        return True

s = input("Please enter an expression : ")
if  checkNesting(s) : print("Expression correctly formed")

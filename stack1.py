"""
stack1.py
interactive demonstration of stacks of strings
created by sands 7/11/10
modified by rturnr 15/11/10
"""

myStack = []

running = True

while running:
    print("\nStack contents:", myStack, "\n")  # generate extra blank lines in output
    line = input("Select an option: push, pop or quit: ")
    if line == "quit":
        running = False
    elif line == "pop":
        if len(myStack) == 0 :
            print("The stack is empty, pop cannot be applied")
        else:
            print("Popped", myStack.pop())
    elif line == "push" :
        myString = input("Enter name to push onto stack: ")
        myStack.append(myString)
    else:
        print("Invalid selection")

"""
search1.py
finds all lines in a file that contain a search string specified by the user
created by sands 29/11/10
"""

fileName = input("Please supply name of input file: ")
gotIt = False
try :
    f = open(fileName)
    gotIt = True
except IOError as e :
    print("Failed to open", fileName)
    
if gotIt :
    lineCount = 0
    string = input("Specify search string: ")
    for line in f :
        lineCount = lineCount+1
        if line.lower().find(string)!=-1 :
            print("The string", '"'+string+'"', "occurs in line", lineCount)

    f.close()

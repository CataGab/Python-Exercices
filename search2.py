"""
search2.py
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
        line = line.lower()
        occs = line.count(string)
        if occs != 0:
            if occs == 1 :
                print("The string", '"'+string+'"', "occurs in line", lineCount)
            else :
                print("The string", '"'+string+'"', "occurs", occs,
                      "times in line", lineCount)
            positions = []
            pos = line.find(string)
            while pos!= -1 :
                positions.append(pos)
                pos = line.find(string, pos+1)
            outString = "at position " + str(positions[0])
            for p in positions[1:] :
                outString = outString + " and " + str(p)
            print(outString)

    f.close()

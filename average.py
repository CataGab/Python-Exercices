"""
average.py
program to calculate average, minimum and maximum of a series of exam marks
created by sands 23/10/10
edited 29/10/10
"""

# initialise total and counter
total = 0.0
count = 0

print("Enter marks one per line")
print("Use a negative number to end")

# get first mark
mark = float(input("Mark: "))

# initialise mini and maxi - I've not used the names min and max as
#                           these are names of built-in functions
mini = mark
maxi = mark

# process mark and get next one
# continue until negative number entered
while mark >= 0 :
    total = total+mark
    if mark>maxi : maxi = mark
    elif mark<mini : mini = mark
    count = count+1
    mark = float(input("Mark: "))

# output average
print("The average mark is", round(total/count, 2))
print("The largest mark was", maxi, "and the smallest mark was", mini)




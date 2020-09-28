"""
people.py
formatted output of names and ages
created by sands 30/10/10
"""
fname1 = input("enter first name person 1 : ")
sname1 = input("enter second name person 1 : ")
age1 = int(input("enter age person 1 : "))
fname2 = input("enter first name person 2 : ")
sname2 = input("enter second name person 2 : ")
age2 = int(input("enter age person 2 : "))

print(format("First name", "12s") + format("Second name", "12s") + format("Age", ">4s"))
print(format("Monty", "12s") + format("Python", "12s") + format(40, "4d"))
print(format("Bart", "12s") + format("Simpson", "12s") + format(13, "4d"))
print(format(fname1, "12.12s") + format(sname1, "12.12s") + format(age1, "4d"))
print(format(fname2, "12.12s") + format(sname2, "12.12s") + format(age2, "4d"))
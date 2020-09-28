"""
hello1.py
greeting program
created by sands 6/10/10
edited by sands 25/10/10
modified by sands 21/10/2013 : code to print "Happy birthday" added
"""

from datetime import date

# get user's name
firstName = input("Please type your first name ")
secondName = input("Please type your surname (family name) ")

# informal greeting
print("\nHello, ", firstName)

# formal greeting
print("\nGood morning, Mr.", firstName[0]+'. '+secondName)

# get date of birth
dobString = input("Please give your date of birth (dd/mm/yyyy) ")
dayString = dobString[0:2]
monthString = dobString[3:5]
yearString = dobString[6:10]

# calculate and display age
age = date.today().year-int(yearString)
birthMonth = int(monthString)
todayMonth = date.today().month
birthDay = int(dayString)
todayDay = date.today().day

# adjust age if this year's birthday has not occurred yet
if birthMonth > todayMonth : age = age-1
elif birthMonth == todayMonth :
    if birthDay > todayDay : age = age -1
    elif birthDay == todayDay : print("Happy birthday!")

#print age in all cases
print("Your age must be", age)

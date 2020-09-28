"""
weight.py
weight conversion program
converts from grams to pounds and ounces
created by sands 14/10/10
"""

grams = int(input("Enter weight in grams: "))

totalOunces = grams * 16 //454

pounds = totalOunces // 16
ounces = totalOunces % 16

print("The weight in ounces is", totalOunces)
print("That is equal to", pounds, "pounds and", ounces, "ounces")

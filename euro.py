"""
euro.py
currency conversion program
created by sands 5/10/10
"""

# get exchange rate
exchangeRateString = input("Enter the exchange rate ")
exchangeRate = float(exchangeRateString)
print("Exchange rate is ", exchangeRate, " euros to the pound")

# get cost of first item
firstCost = float(input("Enter cost of first item "))
print("First item cost", firstCost, "euros")
print("Cost in pounds is", round(firstCost/exchangeRate, 2), "pounds")

# get cost of second item
secondCost = float(input("Enter cost of second item "))
print("Second item cost", secondCost, "euros")
print("Cost in pounds is", round(secondCost/exchangeRate, 2), "pounds")

# get cost of third item
thirdCost = float(input("Enter cost of third item "))
print("Third item cost", thirdCost, "euros")
print("Cost in pounds is", round(thirdCost/exchangeRate, 2), "pounds")

# calculate total cost
totalCost = firstCost+secondCost+thirdCost
print("Total cost is", totalCost, "euros")
print("Total cost in pounds is", round(totalCost/exchangeRate, 2), "pounds")

"""
exercise1.py
currency conversion program
created by sands 5/10/10
modified by sands 1/11/10
"""

# get exchange rate
exchangeRateString = input("Enter the exchange rate ")
exchangeRate = float(exchangeRateString)
print("Exchange rate is ", exchangeRate, " euros to the pound")

print("Use a negative number to terminate input")
running = True
totalCost = 0.0
count = 1

while running :
    # get cost of item - check if its negative
    itemCost = float(input("Cost of item " + str(count) +": "))
    if itemCost < 0 : running = False
    else :
        # output cost in euros and pounds and add to total
        print("Item", count, "cost", itemCost, "euros")
        print("Cost in pounds is", round(itemCost/exchangeRate, 2))
        totalCost = totalCost + itemCost
        count = count + 1

# display total cost in euros and pounds
print("Total cost is", totalCost, "euros")
print("Total cost in pounds is", round(totalCost/exchangeRate, 2))

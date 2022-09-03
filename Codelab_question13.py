"""
Assume that -price- is an integer variable whose value is the price (in US currency) in cents of an item.
Write a statement that prints the value of price in the form of 'X dollars and Y cents' on a line by itself.
So, if the value of -price- was 4321, your code would print '43 dollars and 21 cents'.
"""

price = int(input("Input an integer:"))

dollars = price / 100
cents = (price % 100) // 1

print("%i dollars and %i cents" %(dollars, cents))

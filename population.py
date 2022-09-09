#******************************************************************************
# population.py
#******************************************************************************
# Name: Kun Dong 
#******************************************************************************
# Remarks (optional): 
# Used only 3 variables: P, t, r

# Import math module
import math

# Input a number for initial population
P = float(input("Enter initial population: "))


# Input the numbers for time elapsed and growth rate for the first time
t = float(input("Enter first time period (in years): "))
r = float(input("Enter first growth rate (in percent): "))

# Calculate the population for the first period with the formula
P = P * (math.e) ** (r/100 * t)


# Update the numbers for the second time
t = float(input("Enter second time period (in years): "))
r = float(input("Enter second growth rate (in percent): "))

# Calculate and update the population for the second period
P = P * (math.e) ** (r/100 * t)


# For the third time
t = float(input("Enter third time period (in years): "))
r = float(input("Enter third growth rate (in percent): "))

# Population for the third period
P = P * (math.e) ** (r/100 * t)


# Print the final result of the formula
print("The final population is", P)

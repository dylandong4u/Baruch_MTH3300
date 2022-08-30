"""
a. Create variables called P, r, n and t, which you should assign to be 20, .03, 4 and 8, respectively.
b. Write code to print out the corresponding value of A according to the formula.
"""

P = float(input('Input the value for P: '))
r = float(input('Input the value for r: '))
n = float(input('Input the value for n: '))
t = float(input('Input the value for t: '))

A = P * (1 + (r / n) ** (n * t))

print('A = ', A)

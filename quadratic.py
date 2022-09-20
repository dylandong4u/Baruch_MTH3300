#******************************************************************************
# quadratic.py
#******************************************************************************
# Name: Kun Dong 
#******************************************************************************
# Remarks (optional):

import math

# Input numbers for coefficients
a = float(input("Enter x^2 coefficient: "))
b = float(input("Enter x^1 coefficient: "))
c = float(input("Enter x^0 coefficient: "))


# When b^2 - 4ac > 0, there are two solutions
if (b ** 2 - 4 * a *c) > 0 and a != 0:

    # Possible solutions of quadratic formula
    solution_1 = (-b + math.sqrt((b ** 2 - 4 * a * c))) / (2 * a) 
    solution_2 = (-b - math.sqrt((b ** 2 - 4 * a * c))) / (2 * a)

    print(f'TWO REAL SOLUTIONS: x = {solution_1:.4f} and x = {solution_2:.4f}')

# When b^2 - 4ac = 0, there's only one solution
elif (b ** 2 - 4 * a * c) == 0 and a != 0:

    solution = (-b + math.sqrt((b ** 2 - 4 * a * c))) / (2 * a)
    print(f'ONE SOLUTION: x = {solution:.4f}')

# When a is 0, the formula becomes linear and there's only one solution
elif a == 0:

    solution = -c / b
    print(f'ONE SOLUTION: x = {solution:.4f}')

# Calculate complex solutions
else:

    # Calculate the solutions in two parts
    # The first part
    solution_part_1 = -b / (2 * a)

    # The second part
    # Assume sqrt(-1) is i, sqrt() can't take in negative input so I used abs()
    solution_1_part_2 = - math.sqrt(abs(b ** 2 - 4 * a * c)) / (2 * a)
    solution_2_part_2 = math.sqrt(abs(b ** 2 - 4 * a * c)) / (2 * a)

    # Make sure the printing format is consistent 
    if solution_1_part_2 > 0 and solution_2_part_2 < 0:

        print(f'COMPLEX SOLUTIONS: x = {solution_part_1:.4f}{solution_2_part_2:.4f}i and x = {solution_part_1:.4f}+{solution_1_part_2:.4f}i')

    elif solution_1_part_2 < 0 and solution_2_part_2 > 0:

        print(f'COMPLEX SOLUTIONS: x = {solution_part_1:.4f}{solution_1_part_2:.4f}i and x = {solution_part_1:.4f}+{solution_2_part_2:.4f}i')

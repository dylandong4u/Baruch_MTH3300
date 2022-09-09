#******************************************************************************
# binary.py
#******************************************************************************
# Name: Kun Dong 
#******************************************************************************
# Remarks (optional):
# Only used // for the challenge question...

# 128   64   32   16   8   4   2   1
# 8     7    6    5    4   3   2   1

# Import random module
import random

# Create 8 random integer from 0 and 1 for each digit
bnumber_1 = random.randint(0,1)
bnumber_2 = random.randint(0,1)
bnumber_3 = random.randint(0,1)
bnumber_4 = random.randint(0,1)
bnumber_5 = random.randint(0,1)
bnumber_6 = random.randint(0,1)
bnumber_7 = random.randint(0,1)
bnumber_8 = random.randint(0,1)

print("Here's a random example of binary!")

# Find equivalent decimal number for the random binary number
tnumber = bnumber_8 * 128 + bnumber_7 * 64 + bnumber_6 * 32 + bnumber_5 * 16 + bnumber_4 * 8 + bnumber_3 * 4 + bnumber_2 * 2 + bnumber_1 * 1

print("The binary number", bnumber_8, bnumber_7, bnumber_6, bnumber_5, bnumber_4, bnumber_3, bnumber_2, bnumber_1, "is the same as the decimal number %i." %tnumber)

# Input an integer decimal number to convert into binary 
tnumber = int(input("Now, enter a decimal number between 0 and 255: "))

# Use the decimal number input to find the equivalent binary number in a very .... way
bnumber_8 = tnumber // 128
bnumber_7 = (tnumber - (bnumber_8 * 128)) // 64
bnumber_6 = (tnumber - (bnumber_7 * 64) - (bnumber_8 * 128)) // 32
bnumber_5 = (tnumber - (bnumber_6 * 32) -(bnumber_7 * 64) - (bnumber_8 * 128)) // 16
bnumber_4 = (tnumber - (bnumber_5 * 16) - (bnumber_6 * 32) -(bnumber_7 * 64) - (bnumber_8 * 128)) // 8
bnumber_3 = (tnumber - (bnumber_4 * 8) - (bnumber_5 * 16) - (bnumber_6 * 32) -(bnumber_7 * 64) - (bnumber_8 * 128)) // 4
bnumber_2 = (tnumber - (bnumber_3 * 4) - (bnumber_4 * 8) - (bnumber_5 * 16) - (bnumber_6 * 32) -(bnumber_7 * 64) - (bnumber_8 * 128)) // 2
bnumber_1 = (tnumber - (bnumber_2 * 2) - (bnumber_3 * 4) - (bnumber_4 * 8) - (bnumber_5 * 16) - (bnumber_6 * 32) -(bnumber_7 * 64) - (bnumber_8 * 128)) // 1

print("This number is equivalent to the binary number", bnumber_8, bnumber_7, bnumber_6, bnumber_5, bnumber_4, bnumber_3, bnumber_2, bnumber_1,)
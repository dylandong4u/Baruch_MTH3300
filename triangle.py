#******************************************************************************
# triangle.py
#******************************************************************************
# Name: Kun Dong 
#******************************************************************************
# Remarks (optional):
# Used for-in loop and lots of if to check whether the triangle is valid...

# Import math module
import math

# Input numbers as sidelengths of the triangle
l_length = float(input("Enter largest side length: "))
m_length = float(input("Enter middle side length: "))
s_length = float(input("Enter smallest side length: "))

# Declare 4 criteria to check the validity of the triangle
criteria_1 = 0
criteria_2 = 0
criteria_3 = 0
criteria_4 = 0

# This for-in loop is actually not necessary
# Use for-in loop to check whether the triangle is valid
for i in range (4):
    if l_length >= m_length >= s_length > 0:
        criteria_1 = "valid"

    if l_length + m_length > s_length:
        criteria_2 = "valid"

    if l_length + s_length > m_length:
        criteria_3 = "valid"

    if m_length + s_length > l_length:
        criteria_4 = "valid"

# Check if the triangle satisfies all criteria
if criteria_1 and criteria_2 and criteria_3 and criteria_4 == "valid":

    # Use the law of cosine to find the largest angle in radian  
    cos_l = (m_length ** 2 + s_length ** 2 - l_length ** 2) / (2 * m_length * s_length)
    # Convert radian to degree using: degree = radian / (pi / 180)
    degree_l = math.acos(cos_l) / (math.pi / 180)

    # Use the law of sine to find the middle angle
    sin_m = math.sqrt((1 - cos_l ** 2)) / l_length * m_length
    # Convert radian to degree
    degree_m = (math.asin(sin_m) / (math.pi / 180))

    # Subtract to find the smallest angle
    degree_s = 180 - degree_l - degree_m

    print("The angles are:")
    print(degree_l)
    print(degree_m)
    print(degree_s) 

else: 
    print("There is an error in the input")

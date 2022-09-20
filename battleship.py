#******************************************************************************
# ship.py
#******************************************************************************
# Name: Kun Dong 
#******************************************************************************
# Remarks (optional):
# I used lists for the challenge question...
# All the logic of individal small squares just confused me a lot...
# But the logic became much clearer to me after using lists... 


# Define the validity of three battleships before the if-else statements
validity1 = False
validity2 = False
validity3 = False



# Battleship 1 inputs
ship1_x1 = int(input("Enter x-coordinate of square one: ")) # the first square 
ship1_y1 = int(input("Enter y-coordinate of square one: "))
ship1_x2 = int(input("Enter x-coordinate of square two: ")) # the second square 
ship1_y2 = int(input("Enter y-coordinate of square two: "))

# Battleship 1 selections
if (1 <= ship1_x1 <= 4) and (1 <= ship1_x2 <= 4) and(1 <= ship1_y1 <= 4) and (1 <= ship1_y2 <= 4): # check if the inputs are in the 4 * 4 big square
    if (ship1_x1 == ship1_x2 and abs(ship1_y1 - ship1_y2) == 1) or (ship1_y1 == ship1_y2 and abs(ship1_x1 - ship1_x2) == 1): # check if the little squares in the ship are adjacent
        validity1 = True # if valid, update the boolean value
        print("Valid")
    else:
        print("Non-adjacent squares")
else:
    print("Square(s) not on grid")



# Battleship 2 inputs
ship2_x1 = int(input("Enter x-coordinate of square one: ")) # the first square
ship2_y1 = int(input("Enter y-coordinate of square one: "))
ship2_x2 = int(input("Enter x-coordinate of square two: ")) # the second square
ship2_y2 = int(input("Enter y-coordinate of square two: "))

# Battleship 2 selections
if (1 <= ship2_x1 <= 4) and (1 <= ship2_x2 <= 4) and(1 <= ship2_y1 <= 4) and (1 <= ship2_y2 <= 4): # check if the inputs are in the 4 * 4 big square
    if (ship2_x1 == ship2_x2 and abs(ship2_y1 - ship2_y2) == 1) or (ship2_y1 == ship2_y2 and abs(ship2_x1 - ship2_x2) == 1): # check if the little squares in the ship are adjacent
        validity2 = True # if valid, update the boolean value
        print("Valid")
    else:
        print("Non-adjacent squares")
else:
    print("Square(s) not on grid")



# Battleship 3 inputs
ship3_x1 = int(input("Enter x-coordinate of square one: ")) # the first square
ship3_y1 = int(input("Enter y-coordinate of square one: "))
ship3_x2 = int(input("Enter x-coordinate of square two: ")) # the second square
ship3_y2 = int(input("Enter y-coordinate of square two: "))

# Battleship 3 selections
if (1 <= ship3_x1 <= 4) and (1 <= ship3_x2 <= 4) and(1 <= ship3_y1 <= 4) and (1 <= ship3_y2 <= 4): # check if the inputs are in the 4 * 4 big square
    if (ship3_x1 == ship3_x2 and abs(ship3_y1 - ship3_y2) == 1) or (ship3_y1 == ship3_y2 and abs(ship3_x1 - ship3_x2) == 1): # check if the little squares in the ship are adjacent
        validity3 = True # if valid, update the boolean value
        print("Valid")
    else:
        print("Non-adjacent squares")
else:
    print("Square(s) not on grid")



# Using lists...
# Each ship has two small squares 
ship1 = [[ship1_x1, ship1_y1], [ship1_x2, ship1_y2]]
ship2 = [[ship2_x1, ship2_y1], [ship2_x2, ship2_y2]]
ship3 = [[ship3_x1, ship3_y1], [ship3_x2, ship3_y2]]


# Check if all ships are valid
if (validity1 == True and validity2 == True and validity3 == True):
    # Check if the ships overlap
    # The squares of one ship should not be the same as the squares in other ships
    if (ship1[0] != ship2[0] and ship1[0] != ship2[1]) and (ship1[0] != ship3[0] and ship1[0] != ship3[1]) and (ship1[1] != ship2[0] and ship1[1] != ship2[1]) and (ship1[1] != ship3[0] and ship1[1] != ship3[1]) \
    and (ship2[0] != ship1[0] and ship2[0] != ship1[1]) and (ship2[0] != ship3[0] and ship2[0] != ship3[1]) and (ship2[1] != ship1[0] and ship2[1] != ship1[1]) and (ship2[1] != ship3[0] and ship2[1] != ship3[1]) \
    and (ship3[0] != ship1[0] and ship3[0] != ship1[1]) and (ship3[0] != ship2[0] and ship3[0] != ship2[1]) and (ship3[1] != ship1[0] and ship3[1] != ship1[1]) and (ship3[1] != ship2[0] and ship3[1] != ship2[1]):
        print("All placements are valid and none of the ships overlap")
    else:
        print("Not all placements are valid")
else:
    print("Not all placements are valid")
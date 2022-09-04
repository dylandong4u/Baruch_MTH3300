permit_type = input("permit type (a/f/p/s):")

# the correct answer is to use permit_type = input() to substitute the line above

if permit_type == "a":
    price = 95
    print("$%i" %price)

elif permit_type == "f":
    price = 90
    print("$%i" %price)

elif permit_type == "p":
    price = 50
    print("$%i" %price)

elif permit_type == "s":
    price = 25
    print("$%i" %price)

else:
    print("invalid type")

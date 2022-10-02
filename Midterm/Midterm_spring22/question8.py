def kbuzz(x, k):
    if x % k == 0:
        return True 
    elif str(x)[-1] == str(k):
        return True 
    else:
        return False

import random
int1 = int(input("Enter n: "))
int2 = random.randint(2,9)
print("Random k:", int2)

if kbuzz(int1, int2) == True:
    print("BUZZ")
else:
    print("")

import math

x = float(input(''))
y = float(input(''))

cosx = math.cos(x)
siny = math.sin(y)

if cosx > 0 or siny > 0:
    print("YES")

else:
    print("NO")

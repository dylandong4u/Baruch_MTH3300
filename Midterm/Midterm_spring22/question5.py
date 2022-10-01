nums = [8, 1, 0]
xsum = 4
for n in nums:
    print(xsum, end = '')
    xsum = xsum + n
    if n < 3:
        print(n, '+')
print(xsum)


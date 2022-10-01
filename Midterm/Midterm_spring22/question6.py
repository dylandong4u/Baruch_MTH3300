pq = [10, 15, 8, 6, 4]

product = 1

for i in pq:
    if i >= 10:
        product *= i

print(product)


count = 0

for i in pq:
    if i >= 10:
        count += 1

print(count)

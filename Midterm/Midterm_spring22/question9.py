name1, name2, name3 = input("Enter three names on a line: ").split()

alist = [name1, name2, name3]

for i in alist:
    if i[0] == "x":
        print(i)
        alist.remove(i)

print(alist)

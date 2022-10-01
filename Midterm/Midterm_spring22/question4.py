x = int(input('Enter an int: '))
y = int(input('Enter an int: '))

if x != (y - 2):
    if x > 5:
        print('AB')
    elif x > 7:
        print('CD')

if x >= 10:
    if x > 3 or y > 12:
        print('EF')
    else:
        print('GH')


#******************************************************************************
# missing.py
#******************************************************************************
# Name: Kun Dong 
#******************************************************************************
# Overall notes (not to replace inline comments):
# 

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

names = input("Enter some names on a single line: ").split() # Enter names and separate by space 

for name in names: # Go through each name in the input 
    if name[0] in letters: # Find the initial character of each name
        letters.remove(name[0]) # Remove it from the letter list

# Print results
print("Missing letters:", end=" ")
for i in letters:
    print(i, end=" ")

'''
# Challenge:
for name in names:
    for index in range(len(name)-1): # Find the index of characters in each name except the last one
        if name[index] in letters: # Remove them from the letter list
            letters.remove(name[index])

# Print results
print("Missing letters:", end=" ")
for i in letters:
    print(i, end=" ")
'''
def new_input():
	value = input("Enter two ints: ")
	if len(value) % 2 == 1:
		num1 = int(value[0:len(value) // 2 - 1])
		num2 = int(value[len(value) // 2 + 1 : -1])
	elif len(value) % 2 == 0:
		 for i in value:
			count = 0
			count = count + 1
			if i == ' ':
				print(count)
			
			num1 = int(value[0:count-1])
			num2 = int(value[count+1:-1])
	
	if num1 == num2:
		print(f'Output: {num1}')
	else:
		import random
		if num1 > num2:
			print('Output: ', random.randrange(num2, num1))
		else:
			print('Output: ', random.randrange(num1, num2))

				
new_input(k

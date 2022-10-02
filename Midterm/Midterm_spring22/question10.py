pulse = float(input("Enter pulse: "))

oxygen = float(input("Enter oxygen: "))

ideal_pulse = pulse >= 60 and pulse <= 100
ideal_oxygen = oxygen >= 95 and oxygen <= 100

if ideal_pulse and ideal_oxygen:
	print("SAFE")
else:
	temperature = float(input("Enter temperature: "))
	if temperature < 97 or temperature > 99.5:
		print("ADMIT")

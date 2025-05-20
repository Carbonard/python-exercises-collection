def first_digit(num):
	num = abs(num)
	if num >= 1:
		while num >= 10:
			num //= 10
	else:
		while num < 1:
			num *= 10
	return int(num)

def scientific_notation(num, trunc=16):
	sign = "-" if num < 0 else ""
	num = abs(num)
	exp = 0
	if num >= 1:
		while num >= 10:
			num /= 10
			exp += 1
	elif num > 0:
		while num < 1:
			num *= 10
			exp -= 1
		num = num
	if num == int(num): # To avoid resulst like 2.0
		num = int(num)
	if trunc == 0: trunc -= 1 # To delete the floating point from next string
	result = sign + str(num)[:trunc+2]
	if exp != 0:
		result += f"*10^{exp}"
	return result
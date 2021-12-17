def sum_of_multiples(upper_limit):
	sum = 0
	for i in range(upper_limit):
		if (i%3 == 0) | (i%5 == 0):
			sum += i
		elif (i%3 == 0) & (i%5 == 0):
			sum -= i
	return sum
	
print(sum_of_multiples(1000))

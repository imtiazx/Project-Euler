def nth_Fibonacci_term(n):
	n1 = 1
	n2 = 2
	
	if n < 0:
		print('Enter a positive integer.')
	elif n == 0:
		return 0	
	elif n == 1:
		return n1	
	elif n == 2:
		return n2
	else: 
		for i in range(2, n):
			nth = n1 + n2
			n1 = n2
			n2 = nth	
		return nth
		
def sum_even_Fibonacci_terms(limit):
	sum = 0
	for i in range(100): #large range
		if nth_Fibonacci_term(i) < limit:
			if nth_Fibonacci_term(i)%2 == 0:
				sum += nth_Fibonacci_term(i)		
	return sum

print(sum_even_Fibonacci_terms(4000000))

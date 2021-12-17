def check_prime(n): 
	if n > 1:
		r = int(n**0.5) + 1
		for i in range(2, r):
			if n%i == 0:
				return False
				break
		else:
			return True
	else:
		print("Enter a valid integer!")
			
def largest_prime_factor(num):
	for i in range(2, num):
		if num%i == 0:
			if check_prime(num/i):
				return int(num/i)
				break
				
print(largest_prime_factor(600851475143))

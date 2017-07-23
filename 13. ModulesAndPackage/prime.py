def isPrime(n):
	for x in range(2, int(n / 2 + 1)):
			if not n % x:
				return False
	return True

def primesTo(n):
	for x in range(2, n):
		if isPrime(x):
			print(x)
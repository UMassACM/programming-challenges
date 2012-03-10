import time
start = time.time()

c = 33
n = 1

def isPrime(n):

	if n == 2:
		return True

	if n < 2:
		return False
	
	for i in range(3, int(n**0.5)+1,2):
		if n%i == 0:
			return False
	return True

goo = True

while goo:

	go = not isPrime(c)

	while go:
	
		p = c - 2*n*n
		
		if isPrime(p):
			n = 1
			go = False
		else:
			n += 1

		if p < 0:
			print c
			goo = False
			go = False

	c += 2
print time.time() - start

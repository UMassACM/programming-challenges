import time
start = time.time()

def isPrime(n):
	if n % 2 == 0:
		return False
	
	for i in xrange(3,int(n**0.5)+1,2):
		if n % i == 0:
			return False
	return True

numPrimes = 0
numTotal = 1
depth = 1

while float(numPrimes)/float(numTotal) > 0.1 or depth == 1:

	n = depth
	depth += 1

	q = 4*n*n + 1
	
	if isPrime(q):
		numPrimes +=1

	if isPrime(q + 2*n):
		numPrimes +=1

	if isPrime(q - 2*n):
		numPrimes +=1

	numTotal += 4

print 2*depth - 1
print time.time() - start

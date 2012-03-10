import time, math
start = time.time()

def isPrime(n):

	if n % 2 == 0:
		return False
	
	for i in range(3, int(math.sqrt(n)) + 1, 2):
		if n % i == 0:
			return False
	return True
	
def isPanDigi(digits, n):
	digiSet = set([])
	
	for i in range(len(digits)):
		digiSet.add(digits[i])

	for i in range(1,n+1):
		if str(i) not in digiSet:			
			return False
	return True

for i in range(7654321, 1234567, -1):
	if isPanDigi(str(i), 7) and isPrime(i):
		print i
		break
		
for i in range(4321, 1234, -1):
	if isPanDigi(str(i), 4) and isPrime(i):
		print i
		break
		
print time.time() - start


import time, math
start = time.time()

def isPanDigi(digits):
	digiSet = set([])
	
	for i in range(len(digits)):
		digiSet.add(digits[i])

	for i in range(1,10):
		if str(i) not in digiSet:			
			return False
	return True

products = set([])
sum = 0

for a in range(1, 10**5):
	for b in range():
		p = a * b
		digits = str(a) + str(b) + str(p)
		
		if len(digits) > 9:
			break
		elif len(digits) == 9 and isPanDigi(digits):
			if p not in products:
				sum += p
				products.add(p)

print products
print sum
print time.time() - start
			



	
	

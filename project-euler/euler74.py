import math, time
start = time.time()

def fact(n):
	sum = 0
	while n > 0:
		sum += math.factorial(n%10)
		n //= 10
	return sum

count60 = 0

for i in range(1,10**6):

	n = fact(i)
	terms = set([i])

	while n not in terms:
		terms.add(n)
		n = fact(n)

	if len(terms) == 60:
		count60 += 1

print count60
print time.time() 
	

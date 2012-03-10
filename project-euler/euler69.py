import time
start = time.time()

def factor(n):
	yield 1
	i = 2
	limit = n**0.5
	while i <= limit:
		if n % i == 0:
			yield i
			n /= i
			limit = n**0.5
		else:
			i += 1

	if n > 1:
		yield n

factors = {}
factors[0] = set([0])
factors[1] = set([1])

maxN = 0
high = 0

for i in xrange(2,510510+1):
	factors[i] = set(factor(i))

i = 510510
relPrime = 1
for j in xrange(i,1,-1):
	if len(factors[i].intersection(factors[j])) == 1:
		relPrime += 1

if i/relPrime > maxN:
	maxN = i/relPrime
	high = i

print high
print time.time() - start

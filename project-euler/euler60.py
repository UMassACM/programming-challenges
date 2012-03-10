primes = set(range(2,10000000))

for i in range(2,1001):
	for j in range(2*i,10000000,i):
		primes.discard(j)


primes = list(primes)

primeStrings = []
for num in primes:
	primeStrings.append(str(num))

primeStringsSet = set(primeStrings)

list.sort(primeStrings)

choices = set([])


for i in range(len(primeStrings)-4):
	l = len(primeStrings[i])
	c = 0
	j = 1
	while primeStrings[i+j].startswith(primeStrings[i]):
		if primeStrings[i+j][l::] in primeStringsSet:
			c+=1
		j+=1
	if j >= 4 and c >= 4:
		choices.add(primeStrings[i])

for i in range(len(primeStrings)-4):
	l = len(primeStrings[i])
	c = 0
	j = 1
	while primeStrings[i+j].startswith(primeStrings[i]):
		if primeStrings[i+j][l::] in choices:
			c+=1
		j+=1
	if j >= 4 and c >= 4:
		choices.add(primeStrings[i])

print choices

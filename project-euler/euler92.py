import time
start = time.time()

def nextLink(n):
	sum = 0
	while n > 0:
		sum += (n%10)**2
		n //= 10
	return sum



set89 = set([89])
set1 = set([1])
setAll = set([])



#for i in xrange(1, (9**2)*7 + 1):
#	n = i
#	setTmp = set([n])

#	while (n not in set89) and (n not in set1):
#		n = nextLink(n)
#		setTmp.add(n)

#	if n in set89:
#		set89.update(setTmp)
#	elif n in set1:
#		set1.update(setTmp)


count = 0

for i in xrange(1, 10**7):

	n = i
	
	if (n not in set89) and (n not in set1):
		n = nextLink(n)

	if n in set89:
		count += 1

print count
print time.time() - start
			
	
	

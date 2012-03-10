import time
start = time.time()

pentSet = set(n*(3*n-1)/2 for n in xrange(1,10**6))
max = 10**6 * (3*(10**6)-1)/2


go = True
small = 1000000000

n, m = 2, 1
while go:
	while m < n:
		nn = n * (3*n-1)/2 
		mm = m * (3*m-1)/2
		if nn + mm in pentSet and nn - mm in pentSet:
			print nn - mm
			small = min(small, nn-mm)
			m += 1
			go = False
		else:
			m += 1

	if nn + mm > max:
		print "Too small"
		go = False
		
	n += 1
	m = 1

print small
print time.time() - start
			

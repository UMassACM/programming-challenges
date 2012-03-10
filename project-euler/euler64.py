import time, math
start = time.time()

odd_count = 0

for r in range(2,10**4+1):
	fracs = set([])
	if int(math.sqrt(r)) != math.sqrt(r): #number is not square
		n, d = math.floor(math.sqrt(r)),1
		
		while (n,d) not in fracs:
			fracs.add( (n,d) )
			
			n,d = -n, (r-n*n)/d
			n,d = n-d*int((math.sqrt(r) + n)/d), d
		
		odd_count += (len(fracs)-1) % 2
		
print odd_count
print time.time() - start
		
		

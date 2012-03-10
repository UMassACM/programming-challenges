import time
start = time.time()

def allPrimes(n):
	primes = [1]*n
	primes[0] = 0
	primes[1] = 0
	for i in xrange(2,n):
		for j in xrange(2*i,n,i):
			if primes[i]:
				primes[j] = 0
			else:
				break
	return primes

p = allPrimes(10000000)

def check(n):
	count = 0

	if n[0] != "x":
		for i in range(10):
			tmp = n
			tmp = tmp.replace("x",str(i))
			count += p[int(tmp)]
	else:
		for i in range(1,10):
			tmp = n
			tmp = tmp.replace("x",str(i))
			count += p[int(tmp)]

	if count > 7:
		print n 

#digits = 7
#for i in range(digits-1):
#	for j in range(i+1,digits-1):
#		for k in range(j+1,digits-1):
#			num = ["z"]*digits
#			num[i] = num[j] = num[k] = "x"
#			num = "".join(num)
#			
#			if i:
#				for a in range(1,10):
#					for b in range(10):
#						for c in range(10):
#							tmp = num.replace("z",str(a),1)
#							tmp1 = tmp.replace("z",str(b),1)
#							tmp2 = tmp1.replace("z",str(c),1)
#							for l in [1,3,7,9]:
#								tmpf = tmp1.replace("z",str(l))
#								check(tmpf)	
#			else:
#				for a in range(10):
#					for b in range(10):
#						for c in range(10):
#							tmp = num.replace("z",str(a),1)
#							tmp1 = tmp.replace("z",str(b),1)
#							tmp2 = tmp1.replace("z",str(c),1)
#							for l in [1,3,7,9]:
#								tmpf = tmp1.replace("z",str(l))
#								check(tmpf)



	

print time.time() - start

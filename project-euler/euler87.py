import numpy, time

start = time.time()
def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = numpy.ones(n/3 + (n%6==2), dtype=numpy.bool)
    for i in xrange(1,int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k/3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)/3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]
 
 
LIMIT = 50*(10**6)
primes_two = list(primesfrom2to(int(LIMIT**(1.0/2.0))+1))
primes_three = list(primesfrom2to(int(LIMIT**(1.0/3.0))+1))
primes_four = list(primesfrom2to(int(LIMIT**(1.0/4.0))+1))

print len(primes_two), len(primes_three), len(primes_four), len(primes_two)*len(primes_three)*len(primes_four)
print "Prime time: " + str(time.time()-start)
start = time.time()

valid = set([])
curr_sum = 0

for two in primes_two:
	curr_sum = two*two
	
	if curr_sum > LIMIT:
		continue
		
	for three in primes_three:
		curr_sum = two*two + three*three*three
		
		if curr_sum > LIMIT:
			break
			
		for four in primes_four:
			curr_sum = two*two + three*three*three + four*four*four*four
			
			if curr_sum > LIMIT:
				break
			else:
				valid.add(curr_sum)

print len(valid)
print time.time() -start
				

import numpy, time

def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = numpy.ones(n/3 + (n%6==2), dtype=numpy.bool)
    for i in xrange(1,int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k/3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)/3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]

prime_list = list(primesfrom2to(10**7))
prime_set = set(prime_list)
tot = [0]*(10**7)
tot[1:12] = [1,1,2,2,4,2,6,4,6,4,10] #Initial tot list with first 11 non-zero values. tot[0] = 0



def gcd(a,b):
	while b != 0:
		a,b = b, a%b
	return a

def tot_brute(n):
	count = 1
	for i in range(2,n):
		if gcd(n,i) == 1:
			count += 1
	return count	

def is_perm(a,b):
	for i in range(10):
		if str(a).count(str(i)) != str(b).count(str(i)): #count the number of each digit in each number
			return False
	return True

minimum = 2 ## 2/tot[2] == 2
minimum_n = 2

brute_count = 0

start = time.time()
for n in range(2,10**7):
	
	if n in prime_set:
		tot[n] = n-1
	else:
		for p in prime_list:
		
			factor = 1
			modified = n
			
			if p > n ** 0.5: #The largest prime factor is sqrt(n)
				break

			while modified % p == 0: #factor out all of the smallest p in n
				factor *= p
				modified /= p
			#factor is relatively prime to the modified n, since factor is only made of prime p, and n has no prime p left
			#tot(p*n) = tot(p) * tot(n) if p and n are relatively prime
			if factor == n:
				tot[n] = (p-1) * n / p
				break
			elif factor != 1:
				tot[n] = tot[factor] * tot[modified]
				break

	if float(n)/float(tot[n]) < minimum and is_perm(n,tot[n]):
		minimum = float(n)/float(tot[n])
		minimum_n = n

print minimum_n
print time.time() - start
	

	
	

		



	

	
	
	

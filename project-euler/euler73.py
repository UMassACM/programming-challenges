import time
start = time.time()

def gcd(a,b):
	while b != 0:
		a, b = b, a%b
	return a

fracSet = set()

fracs = []

for den in xrange(2,9):
	for num in xrange(max(int(1.0*float(den)/3.0) - 1,1), min(int(0.5*float(den)) + 1,den)):
		f = gcd(den,num)
		num,den = num/f,den/f
		print num,den

		


print count
print time.time() - start

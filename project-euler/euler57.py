import time
start = time.time()

def twoAndFlip(frac):
	return [frac[1], frac[0] + 2*frac[1]]

def one(frac):
	return [frac[0] + frac[1], frac[1]]

def hasProp(frac):
	if len(str(frac[0])) > len(str(frac[1])):
		return 1
	else:
		return 0

frac = [1,2]
count = 0

for i in xrange(1,1000):
	count += hasProp(one(frac))
	frac = twoAndFlip(frac)

print count
print time.time() - start


		
	

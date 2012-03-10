import time
start = time.time()

def addFlip(whole, frac):
	return [frac[1], frac[0] + whole*frac[1]]

def add(whole, frac):
	return [frac[0] + whole*frac[1], frac[1]]

def digitSum(n):
	sum = 0
	while n > 0:
		sum += n%10
		n //= 10
	return sum

nth = 100

if nth % 3 == 0:
	n = nth/3*2
else
	n = 1

frac = [1,n]

for i in range(nth-1,1,-1):
	if i % 3 == 0:
		frac = addFlip(i/3*2,frac)
	else:
		frac = addFlip(1,frac)

frac = add(2,frac)

print digitSum(frac[0])
print time.time() - start

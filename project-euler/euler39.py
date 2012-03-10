import time
start = time.time()
maxCount, maxP = 0, 0

for p in range(4,100001,2):
	count = 0
	for a in range(1,int(p/3.4)+1):
		b = p * (2*a - p) / (2*(a - p))
		if p*p == 2 * (a*p+b*p-a*b) and int(b) == b:
			count += 1
	if count > maxCount:
		maxCount = count
		maxP = p

print maxP
print time.time()-start

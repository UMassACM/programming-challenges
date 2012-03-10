import time
start = time.time()

closest = [0,0]
diff = 1


for den in xrange(2, 10**3):
	for num in xrange(int(den*3.0/7.0 - 5), int(den*3.0/7.0 + 5)):
	
		tmpDiff = float(3)/float(7) - float(num)/float(den)
		
		if num > 0 and tmpDiff < diff and tmpDiff > 0:
			diff = float(num)/float(den)
			closest = [num, den]

print diff
print closest
print time.time() - start

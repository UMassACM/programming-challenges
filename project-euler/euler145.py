import time
start = time.time()

count = 0;

for i in xrange(1,10**5+1):
	if i%10 != 0 and sum([str(i + int(str(i)[-1::-1])).count(str(digit)) for digit in [0,2,4,6,8]]) == 0:
		count += 1

print count
print time.time()-start

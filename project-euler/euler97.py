import time
start = time.time()

num = 28433

for i in xrange(1,7830458):
	num *= 2
	num %= 10**10

print num + 1
print time.time() - start

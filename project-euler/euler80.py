import time
from decimal import *
start = time.time()
getcontext().prec = 20000

sum = 0

for i in range(1,101):

	n = str(Decimal(i).sqrt())
	n = n.replace(".","")

	for j in range(min(len(n),1000)):
		sum += int(n[j])

print sum - 46
print time.time() - start

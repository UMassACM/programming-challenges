import time
start = time.time()

def factor(n):
	i = 2
	limit = n**0.5
	while i <= limit:
		if n % i == 0:
			yield i
			n /= i
			limit = n**0.5
		else:
			i += 1

	if n > 1:
		yield n

count = 0
low = 0
num = 2

while count < 4:
	factors = set(factor(num))
	if len(factors) == 4:
		count += 1		
		if count == 1:
			low = num	
	else:
		count = 0
		
	num += 1

print low
print time.time() - start

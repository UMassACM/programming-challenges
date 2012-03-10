import time
start = time.time()

def digitCount(n):
	digits = [0]*10
	while n > 0:
		digits[n%10] += 1
		n //= 10

	for i in range(len(digits)):
		digits[i] = str(digits[i])
	
	digits = "".join(digits)
	return digits

def commas(q):
	count = 0
	for i in range(len(q)):
		if q[i] == ",":
			count += 1
	return count
		

digitSet = set()
digitList = []
digitDict = {}
count = 0

for n in xrange(1,10**4):
	m = digitCount(n**3)
	if m in digitDict:
		digitDict[m] += str(n**3) + ","
	else:
		digitDict[m] = str(n**3) + ","
	
low = 10**15
for q in digitDict.items():
	if commas(q[1]) == 5:
		z = q[1][0:-1]
		for i in z.split(","):
			low = min(int(i),low)

print low

print time.time() - start

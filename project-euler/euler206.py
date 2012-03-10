import time
start = time.time()

def good(n):
	n //= 100

	for i in range(9,0,-1):
		if n % 10 == i:
			n //= 100
		else:
			return False
	return True

for d1 in xrange(1,10):
	for d2 in xrange(0,10):
		for d3 in xrange(0,10):
			for d4 in xrange(0,10):
				for d5 in xrange(0,10):
					for d6 in xrange(0,10):
						for d7 in xrange(0,10):
							for d8 in xrange(0,10):
								n = int(str(d1) + str(d2)+str(d3)+str(d4) + str(d5) + str(d6) + str(d7) + str(d8) + str(7) + str(0))
								if good(n*n):
									print n
									print time.time() - start
								n = int(str(d1) + str(d2) + str(d3) + str(d4) + str(d5) + str(d6) + str(d7) + str(d8) + str(3) + str(0))
								if good(n*n):
									print n
									print time.time() - start


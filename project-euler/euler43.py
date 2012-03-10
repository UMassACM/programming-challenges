import time
start = time.time()

def prop(n1, n2):
	n1 //= 10
	n2 %= 100
	return n1 == n2

def diffDigs(a,b,c):

	a1 = str(a)
	while len(a1) < 3:
		a1 = "0" + a1

	b1 = str(b)
	while len(b1) < 3:
		b1 = "0" + b1

	c1 = str(c)
	while len(c1) < 3:
		c1 = "0" + c1

	strg = c1 + b1 + a1
	

	digs = set([])
	
	for i in range(len(strg)):
		if strg[i] in digs:
			return 0
		else:
			digs.add(strg[i])

	if len(digs) < 9:
		return 0
	
	for i in range(0,10):
		if str(i) not in digs:
			strg = str(i) + strg
			break
	
	return int(strg)


sum = 0

for i in range(17, 999, 17):
	for j in range(13, 999, 13):
		if prop(i, j):
			for k in range(11, 999, 11):
				if prop(j,k):
					for l in range(7, 999, 7):
						if prop(k,l):
							for m in range(5, 999, 5):
								if prop(l,m):
									for n in range(3, 999, 3):
										if prop(m,n):
											for o in range(2, 999, 2):
												if prop(n,o):
													q = diffDigs(i,l,o)
													if q:
														sum += q
print sum
print time.time() - start

import time,math
start = time.time()

mindiff = 2000000
area = 0

for w in range(2, 2000):
	for l in range(1,52):
		q = math.fabs(2000000 - w*(w+1)*l*(l+1)/4)
		if mindiff > q:
			mindiff = q
			area = (w*l,w,l,mindiff)

print area

print time.time()-start

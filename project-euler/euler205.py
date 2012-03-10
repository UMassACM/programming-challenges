import time
start = time.time()

d = [0]*9
pTot = [0]*37

for d[0] in range(1,5):
	for d[1] in range(1,5):
		for d[2] in range(1,5):
			for d[3] in range(1,5):
				for d[4] in range(1,5):
					for d[5] in range(1,5):
						for d[6] in range(1,5):
							for d[7] in range(1,5):
								for d[8] in range(1,5):
									tot = 0
									for i in range(9):
										tot += d[i]
									pTot[tot] += 1

d = [0]*6
cTot = [0]*37

for d[0] in range(1,7):
	for d[1] in range(1,7):
		for d[2] in range(1,7):
			for d[3] in range(1,7):
				for d[4] in range(1,7):
					for d[5] in range(1,7):
						tot = 0
						for i in range(6):
							tot += d[i]
						cTot[tot] += 1

pPos = 4**9
cPos = 6**6

pete = [0]*37

for i in range(4,37):
	cProb = 0
	for j in range(6,i):
		cProb += cTot[j]
	pete[i] = cProb * pTot[i]

print sum(pete)/(float(pPos) * float(cPos))
print time.time() - start

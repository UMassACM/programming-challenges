import time, math
start = time.time()

aiPn = {}
aiPn[0] = 1

def P(n):
	parts = 0

	if n < 0:
		return 0

	if n in aiPn and aiPn[n] > 0:
		return aiPn[n]

	Pn = 0
	for k in range(1,int(math.sqrt(n))+1):
		n1 = n - k * (3*k-1)/2
		n2 = n - k * (3*k+1)/2

		Pn1 = P(n1)
		Pn2 = P(n2)

		if k%2 == 1:
			Pn = Pn + Pn1 + Pn2
		else:
			Pn = Pn - Pn1 - Pn2

	aiPn[n] = Pn
	return Pn

n = 1

while P(n) % 1000000 != 0:
	n += 1

print n
print time.time() - start

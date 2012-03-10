import math, time

begin = time.time()
max = 0
d = 0

for i in range(2, 10000):

	noRepeat = True	
	start = math.pow(10,(math.floor(math.log10(i-0.1))+1))
	r = set([start])
	length = 0
	mark = []
	rem = start

	while noRepeat:

		if length > i:
			break
		
		if rem < i:
			rem *= 10
			r.add(rem)
		else:
			rem %= i

		try:
			if rem == mark[0]:
				if max < length:
					max = length
					d = i
				noRepeat = False
		except:
			pass
			
		if rem in r:
			length += 1
			mark.append(rem)

		if rem == 0:
			noRepeat = False
		

print d
print time.time() - begin

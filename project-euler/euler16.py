num = 2**1000
numS = str(num)

sum = 0
for i in range(len(numS)):
	sum += int(numS[i])

print numS[-1]
print sum

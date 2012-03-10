from math import *w

num = factorial(100)
numS = str(num)

sum = 0
for i in range(len(numS)):
	sum += int(numS[i])

print numS[-1]
print sum

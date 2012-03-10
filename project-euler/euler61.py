import math

shape = [None]*6
first, last = [None]*6, [None]*6

for i in range(6):
	shape[i] = set([])
	first[i] = set([])
	last[i] = set([])

#Shape Numbers take the form of: n * (a*n + b) / 2, with a+b=2
#Tri, a = 1; Sqr, a = 2; Pent a = 3; etc
for a in range(1,7):
	b = 2 - a
	
	#We only want values of n that will give numbers [1000,9999]
	low = math.ceil((-b + math.sqrt(b**2 + 8000*a))/(2*a))
	high = math.ceil((-b + math.sqrt(b**2 + 80000*a))/(2*a))
	
	for n in range(int(low),int(high)):
		num = n*(a*n+b)/2

		if num % 10 != 0:
			first[a-1].add(num//100)
			last[a-1].add(num%100)
			shape[a-1].add(num)

for k in range(5):
	for i in range(6):
		tmpFirst = set([])
		tmpLast = set([])

		for j in range(6):
			#get all the first/last of the other shapes
			if j != i:
				tmpFirst = tmpFirst.union(first[j])
				tmpLast = tmpLast.union(last[j])
		tmpShape = set([]).union(shape[i])
		#If a number has no chance for being cyclic, get rid of it
		for num in shape[i]:
			if num//100 not in tmpLast or num%100 not in tmpFirst:
				tmpShape.remove(num)
		shape[i] = tmpShape
		
		#Update first[i], last[i]
		first[i] = set([])
		last[i] = set([])
		for num in shape[i]:
			first[i].add(num//100)
			last[i].add(num%100)	

#At this point, shape[i] only contains numbers that are cyclic with at least one other type of shape, and first and last only contain the first/last digits of numbers in shape



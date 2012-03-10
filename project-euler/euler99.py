import math, time
start = time.time()

bigline = 0
line = 1
fileq = open("e:\dropbox\python\projecteuler\\base_exp.txt")

big = [1,1]
curr = []

baseExp = fileq.readline()
pair = baseExp.split(",")
curr = [float(pair[0]), float(pair[1])]


if big[1] > curr[1]:
	if math.pow(curr[0],curr[1]/big[1]) > big[0]:
		big = curr
		bigline = line
else:
	if math.pow(big[0],big[1]/curr[1]) < curr[0]:
		big = curr
		bigline = line

baseExp = fileq.readline()

while baseExp:

	pair = baseExp.split(",")
	curr = [float(pair[0]), float(pair[1])]
	line += 1

	if big[1] > curr[1]:
		if math.pow(curr[0],curr[1]/big[1]) > big[0]:
			big = curr
			bigline = line
	else:
		if math.pow(big[0],big[1]/curr[1]) < curr[0]:
			big = curr
			bigline = line

	baseExp = fileq.readline()
	print big

print bigline
		

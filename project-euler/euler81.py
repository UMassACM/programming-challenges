import time
start = time.time()

mat = open("e:\dropbox\python\projecteuler\matrix.txt")

rows = [80]*80

for i in xrange(0,80):
	rows[i] = mat.readline()

matrix = []

for i in rows:
	matrix.append(i.split(","))

for i in range(0,80):
	for j in range(0,80):
		matrix[i][j] = int(matrix[i][j])


cost = [[0]*80]*80

for i in xrange(1,80):
	cost[0][i] = cost[0][i-1] + matrix[0][i-1]
	cost[i][0] = cost[i-1][0] + matrix[i-1][0]

for y in range(1,80):
	for x in range(1,80):
		cost[y][x] = min(cost[y-1][x] + matrix[y-1][x], cost[y][x-1] + matrix[y][x-1])


print cost[-1][-1] + matrix[-1][-1]
print time.time() - start
		
	

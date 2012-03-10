import time
start = time.time()
tri = open("e:\dropbox\python\projecteuler\\triangles.txt")

points = tri.readline()
points = points.split(",")
yint1 = yint2 = yint3 = 0
print points

count = 0

while points:
	for i in xrange(len(points)):
		points[i] = int(points[i])

	if points[0]*points[2] <= 0:
		yint1 = points[1] - points[0]*(points[1] - points[3])/(points[0] - points[2])

	if points[2]*points[4] <= 0:
		yint2 = points[3] - points[2]*(points[3] - points[5])/(points[2] - points[4])

	if points[4]*points[0] <= 0:
		yint3 = points[5] - points[4]*(points[5] - points[1])/(points[4] - points[0])

	if not yint1:
		if yint2 * yint3 < 0:
			count += 1

	if not yint2:
		if yint1 * yint3 < 0:
			count += 1

	if not yint3:
		if yint1 * yint2 < 0:
			count += 1

#	if points[1] == 0 or points[3] == 0 or points[5] == 0:
#		count += 1
#		print points

	print count
	yint1 = yint2 = yint3 = 0
	points = tri.readline()
	points = points.split(",")


print count
print time.time() - start

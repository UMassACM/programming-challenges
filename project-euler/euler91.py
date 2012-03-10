import time
start = time.time()

rights = 0

for x1 in range(51):
	for y1 in range(51):
		for x2 in range(x1,51):
			for y2 in range(y1+1):
				if x1 != x2 or y1 != y2:
					if x1 + y1 !=0 and x2 + y2 != 0:
						if not x1*x2 + y1*y2 or not x2*x2 - x1*x2 + y2*y2 - y1*y2 or not -x1*x1 + x1*x2 - y1*y1 + y1*y2:
							rights += 1
							
print rights
print time.time() - start

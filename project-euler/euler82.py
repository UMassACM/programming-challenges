import time



input = open("matrix.txt")

all_rows = input.readlines()

init = [row.split(",") for row in all_rows] ##matrix with initial values

##Make all the entries in init integers
for row in range(len(init)):
	for col in range(len(init[row])):
		init[row][col] = int(init[row][col])

##Initialize the final matrix	
final = []

for row in range(len(init)):
	tmp = []
	for col in range(len(init[0])):
		tmp.append(0)
	final.append(tmp)		

##The first column in the final is the same as the first column in the initial
for row in range(len(init)):
	final[row][0] = init[row][0]

start = time.time()
##Find the cheapest path
for col in range(1,len(init[0])):
	for row in range(len(init)):
		low_cost = final[row][col-1]
		
		for row_comp in range(row, -1, -1):
			cost = final[row_comp][col-1]
			
			for row_temp in range(row_comp,row):
				cost += init[row_temp][col]
				
				if cost > low_cost:
					break
			
			if cost > low_cost:
				continue
			else:
				low_cost = cost
		
		for row_comp in range(row, len(init)):
			cost = final[row_comp][col-1]
			
			for row_temp in range(row+1, row_comp+1):
				cost += init[row_temp][col]
				
				if cost > low_cost:
					break
			
			if cost > low_cost:
				continue
			else:
				low_cost = cost
		
		final[row][col] = low_cost + init[row][col]

min_cost = float("inf")
for row in range(len(init)):
	min_cost = min(min_cost, final[row][-1])

print min_cost
print time.time() - start

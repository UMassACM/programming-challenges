import time
start = time.time()

p1 = p2 = p5 = p10 = p20 = p50 = p100 = p200 = 0

count = 0
rem = 200

for p200 in range(0,1+1):
	for p100 in range(0, (200-200*p200)//100+1):
		for p50 in range(0,(200-200*p200-100*p100)//50+1):
			for p20 in range(0,(200-200*p200-100*p100-50*p50)//20+1):
				for p10 in range(0,(200-200*p200-100*p100-50*p50-20*p20)//10+1):
					for p5 in range(0,(200-200*p200-100*p100-50*p50-20*p20-10*p10)//5+1):
						for p2 in range(0,(200-200*p200-100*p100-50*p50-20*p20-10*p10-5*p5)//2+1):

							p1 = 200 - (2*p2 + 5*p5 + 10*p10 + 20*p20 + 50*p50 + 100*p100 + 200*p200)				
								
							if p1 >= 0 and p1 <=200:
								count += 1
							elif p1 < 0:
								break

print count
print time.time() - start
							

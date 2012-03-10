import time
start = time.time()


def isPanDigi(digits):
	digiSet = set([])
	
	for i in range(len(digits)):
		digiSet.add(digits[i])

	for i in range(1,10):
		if str(i) not in digiSet:			
			return False
	return True

def maxNum(listNums):
	listNums.sort()

	for i in range(len(listNums)):
		if len(str(listNums[-1])) > len(str(listNums[i])):
			listNums[i] *= 10

	listNums.sort()

	for i in range(len(listNums)):
		if listNums[i] % 10 == 0:
			listNums[i] //= 10

	maxNumStr = ''

	for i in listNums[::-1]:
		maxNumStr += str(i)

	return int(maxNumStr)

max = 0
max2 = 0

for i in range(1,10**4):

	strNum = ''
	listNum = []
	j = 1
	
	while len(strNum) < 9:
		strNum += str(i*j)
		listNum.append(i*j)
		j += 1

	if len(strNum) == 9 and isPanDigi(strNum):
		if int(strNum) > max:
			max = int(strNum)
			max2 = i

print max, max2
print time.time() - start
		
	

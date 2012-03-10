import time
start = time.time()

enc = open("e:\dropbox\python\projecteuler\cipher1.txt")
line = enc.readline()

num = line.split(",")
word = ''
bible = ''
continues = True

for i in range(ord('a'),ord('z')+1):
	for j in range(ord('a'),ord('z')+1):
		for k in range(ord('a'),ord('z')+1):
			if continues:
				for m in range(len(num)):
					if m % 3 == 0:
						word += chr(int(num[m]) ^ i)			
					elif m % 3 == 1:
						word += chr(int(num[m]) ^ j)
					else:
						word += chr(int(num[m]) ^ k)

				if word.find(" the ") != -1:
					sum = 0
					for i in range(len(word)):
						sum += ord(word[i])
					print sum
					print time.time() - start
					continues = False
					
				word = ''

print time.time() - start

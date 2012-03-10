import time
start = time.time()

triSet = set([])

for i in range(1,48):
	triSet.add(int(i*(i+1)/2))

def wordToNum(word):
	sum = 0
	for i in range(len(word)):
		sum += ord(word[i]) - ord("A") + 1
	return sum

words = open("e:\dropbox\python\projecteuler\words.txt")

line = words.readline()

wordList = line.split(",")

for i in range(len(wordList)):
	wordList[i] = wordList[i][1:-1]

count = 0

for word in wordList:
	if wordToNum(word) in triSet:
		count += 1

print count
print time.time() - start








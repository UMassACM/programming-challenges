import time
start = time.time()

rank = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "J":11, "Q":12, "K":13, "A":14}

def cardNum(card):
	return rank[card[0:-1]]

def handNum(hand):
	handNums = []
	for card in hand:
		handNums.append(cardNum(card))
	handNums.sort()
	return handNums

def isStraightFlush(hand):
	a = isStraight(hand)
	b = isFlush(hand)
	if a and b:
		return a + b

def isFourKind(hand):
	handNums = handNum(hand)

	n = handNums[0]
	count = 0	
	for i in range(0,4):
		if handNums[i] == n:
			count += 1
	if count == 4:
		return n

	n = handNums[4]
	count = 0
	for i in range(1,5):
		if handNums[i] == n:
			count += 1
	if count == 4:
		return n

def isFullHouse(hand):
	handNums = handNum(hand)
	
	if handNums[0] == handNums[1] and handNums[3] == handNums[4]:
		if handNums[2] == handNums[1] or handNums[2] == handNums[3]:
			return handNums[2]
	return 0
			

def isFlush(hand):
	suit = hand[0][-1]
	for card in hand:
		if card[-1] != suit:
			return 0
	return 1
		

def isStraight(hand):
	handNums = handNum(hand)
	low = handNums[0]
	for i in range(len(handNums)):
		if handNums[i] != low + i:
			return 0
	return low + 4		

def isThreeKind(hand):
	handNums = handNum(hand)

	n = handNums[0]
	count = 0	
	for i in range(0,3):
		if handNums[i] == n:
			count += 1
	if count == 3:
		return n

	n = handNums[1]
	count = 0
	for i in range(1,4):
		if handNums[i] == n:
			count += 1
	if count == 3:
		return n

	n = handNums[2]
	count = 0
	for i in range(2,5):
		if handNums[i] == n:
			count += 1
	if count == 3:
		return n

def isTwoPair(hand):
	handNums = handNum(hand)
	
	tmpHand = []
	tmpCard = 0

	for i in range(len(handNums)):
		tmpCard = handNums.pop(i)

		if handNums[0] == handNums[1] and handNums[2] == handNums[3]:
			return handNums[3]
		else:
			handNums.insert(i, tmpCard)

	return 0

def isPair(hand):
	handNums = handNum(hand)

	for i in range(1, len(hand)):
		if handNums[i-1] == handNums[i]:
			return handNums[i]
	
def highCard(hand):
	return handNum(hand)[-1]

def value(hand):

	val = 0

	SF = isStraightFlush(hand)
	if not val and SF:
		val = 900 + SF

	FK = isFourKind(hand)
	if not val and FK:
		val = 800 + FK

	FH = isFullHouse(hand)
	if not val and FH:
		val = 700 + FH

	F = isFlush(hand)
	if not val and F:
		val = 600 + F

	S = isStraight(hand)
	if not val and S:
		val = 500 + S

	TK = isThreeKind(hand)
	if not val and TK:
		val = 400 + TK

	TP = isTwoPair(hand)
	if not val and TP:
		val = 300 + TP

	P = isPair(hand)
	if not val and P:
		val = 200 + P

	HC = highCard(hand)
	if not val:
		val = HC

	return val

#print value(["2S","2C","2D","7C","8C"])

allHands = open("e:\dropbox\python\projecteuler\poker.txt")

twoHands = allHands.readline()

p1Wins = 0
p2Wins = 0

while twoHands:
	p1 = twoHands.split()[0:5]
	p2 = twoHands.split()[5::]

	if value(p1) > value(p2):
		p1Wins += 1
	else:
		p2Wins += 1

	twoHands = allHands.readline()

print p1Wins
print p2Wins
print 100.0*float(p1Wins)/float(p1Wins + p2Wins)
print time.time() - start







	
		
	
	


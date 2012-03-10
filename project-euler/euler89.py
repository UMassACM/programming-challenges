import time
start = time.time()

input = open("roman.txt")

#Convert an Arabic number to Roman Numerals
def toRoman(n):
	RomanNumerals = [("M",1000), ("CM",900), ("D",500), ("CD",400), ("C",100), ("XC",90), ("L",50), ("XL",40), ("X",10), ("IX",9), ("V",5), ("IV",4), ("I",1)]
	
	roman = ""
	
	for (key,value) in RomanNumerals:
		while n >= value:
			roman += key
			n -= value
	
	return roman

#Convert a Roman Numeral to an Arabic number
def toArabic(n):
	RomanNumerals = [("M",1000), ("CM",900), ("D",500), ("CD",400), ("C",100), ("XC",90), ("L",50), ("XL",40), ("X",10), ("IX",9), ("V",5), ("IV",4), ("I",1)]
	
	arabic = 0
	
	for (key,value) in RomanNumerals:
		while n.startswith(key):
			arabic += value
			n = n[len(key):] #Remove the key from the beginning
	
	return arabic
	

excess = 0

roman_old = input.readline()
roman_old = roman_old[:-2] #remove the trailing /n

while roman_old:
	roman_new = toRoman(toArabic(roman_old))

	if len(roman_new) > len(roman_old):
		print "ERROR"
	excess += len(roman_old) - len(roman_new)
	roman_old = input.readline()
	
	if roman_old.count("\n"):
		roman_old = roman_old[:-2] #remove the trailing /n


print excess
print time.time() - start
	

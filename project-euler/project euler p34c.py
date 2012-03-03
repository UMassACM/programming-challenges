#!/usr/bin/env python2.7

# Find the sum of all numbers which are equal to
# the sum of the factorial of their digits.
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

# the key insight to the speedup of this solution over the
# simple implementation is that the sum of the factorials of the digits
# problem has substructure ordered by the number of digits in a number.
# a lookup table can be made through dynamic programming, and
# then indexing and difference tricks can be used to search spans of
# 10,0000 numbers

import math
from math import factorial, log

# calculate factorial lookup table for 1-9
factorials = [None] * 10**4
for i in range(10):
  factorials[i] = math.factorial(i)

# calculate upper bound on numbers with the desired property,
# based on relation of maximum factorial sums (all 9s) and the number
# of digits: solve d*9! = 10**d -> d = log(9!)/log(10) + 1
limit_pow = int(log(factorials[9])/log(10) + 1)
limit = 10**limit_pow

curious = []

# expand lookup table to cover all 10 <= n <= 10**4,
# checking each table member for the curious property
for i in range(1, 10):
  ten = 10 * i
  for j in range(10):
    ten_one = ten + j
    hun_ten = 10 * ten_one
    factorials[ten_one] = factorials[ten/10] + factorials[j]
    if factorials[ten_one] == ten_one: curious.append(ten_one)
    for k in range(10):
      hun_ten_one = hun_ten + k
      thou_hun_ten = 10 * hun_ten_one
      factorials[hun_ten_one] = factorials[ten_one] + factorials[k]
      if factorials[hun_ten_one] == hun_ten_one: curious.append(hun_ten_one)
      for l in range(10):
        thou_hun_ten_one = thou_hun_ten + l
        factorials[thou_hun_ten_one] = factorials[hun_ten_one] + factorials[l]
        if factorials[thou_hun_ten_one] == thou_hun_ten_one:
          curious.append(thou_hun_ten_one)

# create reverse lookup for lower four digits of n > 10**4
reverse_factorials = {}
for i in xrange(len(factorials)):
  # handle the lower four digits that are dropped in cache access,
  # adding the leading zeros (since 0! = 1)
  if i < 10:
      zeros = 3
  elif i < 100:
      zeros = 2
  elif i < 1000:
      zeros = 1
  else:
      zeros = 0
  d = i - factorials[i] - zeros
  if d in reverse_factorials:
      reverse_factorials[d].append(i)
  else:
      reverse_factorials[d] = [i]

for n in xrange(10**4, limit, 10**4): # 1!, 2! excluded since they are not sums
  diff = factorials[n / 10**4] - n
  if diff in reverse_factorials:
    for num in reverse_factorials[diff]:
      curious.append(n + num)

print sum(curious)

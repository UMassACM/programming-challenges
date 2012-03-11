#!/usr/bin/env python2.7

# Find the sum of all numbers which are equal to
# the sum of the factorial of their digits.
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

# this solution reaches the answer by pure dynamic programming
# on the factor sums and takes ~2 seconds

from math import factorial, log

curious = []

# calculate upper bound on numbers with the desired property,
# based on relation of maximum factorial sums (all 9s) and the number
# of digits: solve d*9! = 10**d -> d = log(9!)/log(10) + 1
limit_pow = int(log(factorial(9))/log(10) + 1)
limit = 10**limit_pow

# initialize factorial table to single digits, zeros
factorials = { tuple(str(i)) : factorial(i) for i in range(10) }
for i in range(2,limit_pow):
  factorials[tuple('0',)*i] = i

# fill factorial sum table for whole range by dynamic programming
for n in xrange(10, limit):
  n_sorted = sorted(str(n))
  try:
    if n == factorials[tuple(n_sorted)]:
      curious.append(n)
      continue
  except:
    fact_sum = factorials[tuple(n_sorted[:-1])] + factorials[tuple(n_sorted[-1])]
    factorials[tuple(n_sorted)] = fact_sum
    if fact_sum == n:
      curious.append(n)

print sum(curious)

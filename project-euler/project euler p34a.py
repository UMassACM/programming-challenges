#!/usr/bin/env python2.7

# Find the sum of all numbers which are equal to
# the sum of the factorial of their digits.
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

# simple solution: derive upper bound and check all candidate n < bound

import math
from math import factorial, log

# calculate factorial lookup table for 1-9
factorials = { str(i) : math.factorial(i) for i in range(10) }

# calculate upper bound on numbers with the desired property,
# based on relation of maximum factorial sums (all 9s) and the number
# of digits: solve d*9! = 10**d -> d = log(9!)/log(10) + 1
limit_pow = int(log(factorials['9'])/log(10) + 1)
limit = 10**limit_pow

sum_curious = 0
for n in xrange(3, limit): # 1! and 2! excluded since they are not sums
  factorial_sum = sum([factorials[i] for i in str(n)])
  if factorial_sum == n:
    sum_curious += n

print sum_curious

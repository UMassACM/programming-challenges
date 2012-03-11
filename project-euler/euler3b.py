#!/usr/bin env python2.7

# determine largest prime factor of 600851475143

import sys
import math

# target number
n = 600851475143

# no factors can be greater than the square root
factor_ceiling = int(math.sqrt(n))

# optimization: handle case of 2 separately, so tests can advance
# by two rather than one
if n % 2 == 0:
  while n % 2 == 0:
    n /= 2
  last_factor = 2
else:
  last_factor = 1

factor = 3

'''
test each possible odd factor, dividing out each,
until the target has either been divided to 1 or
the factor ceiling (square root of target) has
been reached
'''
while n > 1 and factor <= factor_ceiling:
  if n % factor == 0:
    while n % factor == 0:
      n /= factor
    last_factor = factor
  factor += 2

print last_factor

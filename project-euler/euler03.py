#!/usr/bin env python2.7

# determine largest prime factor of 600851475143

import math

FACTOR_TARGET = 600851475143

def is_prime(num):
  if num == 2: return True

  for factor in xrange(2, int(math.sqrt(num))):
    if num % factor == 0:
      return False

  return True

test_factor = 2
factor_ceiling = int(math.sqrt(FACTOR_TARGET))

max_factor = test_factor

while test_factor <= factor_ceiling:
  while not is_prime(test_factor):
    test_factor += 1

  if FACTOR_TARGET % test_factor == 0:
    max_factor = test_factor

  test_factor += 1

print max_factor

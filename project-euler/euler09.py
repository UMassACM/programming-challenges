#!/usr/bin/env python2.7

# find the pythagorean triplet s.t. a + b + c = 1000 and calculate
# the product of a, b, c

target_sum = 1000

for c in range(998, 0, -1):
  ab_sum = target_sum - c
  for a in range(1, ab_sum / 2 + 1):
    b = ab_sum - a
    if a**2 + b**2 == c**2:
      print a*b*c
      exit()

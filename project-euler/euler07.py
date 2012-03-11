#!/usr/bin env python2.7

from __future__ import division
from math import log

# determine nth prime number for n = 10001
# by use of Sieve of Eratosthenes and
# underestimated upper limit for its value

n = 10001

# n / log(n) is an underestimate for the number of primes < n
# finding an upper limit s. t. n / log(n) > 1000 gives a sieve size
limit = n
while int(limit / log(limit)) < n:
  limit += 1
print "the %dth prime number is less than %d" % (n, limit)

# as the estimate is an underestimate, the sieve of Eratosthenes of this size
# is guaranteeed to reveal the desired nth prime

# first assume all numbers >= 2 are prime
primes = [True] * limit
primes[0] = False
primes[1] = False

# preliminarily cross out all the even numbers after two,
# because they cannot be prime
for x in xrange(4, limit, 2):
  primes[x] = False

# with the even numbers dispatched, check for odd numbers that
# have not been crossed out after each round. Each such number
# is a prime. Its odd multiples must be crossed out to continue
# the process until the sieve has found the nth prime
num_primes = 1
for p in xrange(3, limit, 2):
  # for each prime...
  if primes[p]:
    # ...cross out its multiples
    # starting w/ the square of the prime because all numbers lower
    # will already be crossed out and incrementing
    # by 2p to skip over even multiples
    for x in xrange(p**2, limit, p*2):
      primes[x] = False

    # ...and record it
    num_primes += 1
    if num_primes == n:
      print p
      exit()

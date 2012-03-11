#!/usr/bin env python2.7

from math import log

# sum all primes below two million
n = 2*10**6

# n / log(n) is an underestimate for the number of primes < n,
# but still much smaller than n, so twice this quantity will be the sieve size
# limit = int(n / log(n)) * 2

# first assume all numbers >= 2 are prime
primes = [True] * n
primes[0] = False
primes[1] = False

# preliminarily cross out all the even numbers after two,
# because they cannot be prime
for x in xrange(4, n, 2):
  primes[x] = False

# with the even numbers dispatched, check for odd numbers that
# have not been crossed out after each round. Each such number
# is a prime. Its odd multiples must be crossed out to continue
# the process until the sieve has found the nth prime
prime_sum = 2
for p in xrange(3, n, 2):
  # for each prime...
  if primes[p]:
    prime_sum += p

    # ...cross out its multiples
    # starting w/ the square of the prime because all numbers lower
    # will already be crossed out and incrementing
    # by 2p to skip over even multiples
    for x in xrange(p+p*2, n, p*2):
      primes[x] = False

print prime_sum

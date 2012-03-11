#!/usr/bin/env python2.7

# identify the first triangular number to have more than five hundred divisors
limit = 500

def calc_prime_factors(n):
  '''
  calculate the prime factorization of an integer n
  as a dictionary of factors:exponents

  tests all possible factors and repeatedly divides them out of n
  whenever a divisor is found
  '''
  factors = {}
  factor_limit = int(n**.5)

  # one's prime factorization is 1 by definition
  if n == 1:
    return {1 : 0}

  # no even number (after 2) can be a prime factor, so only test 2 & odds
  if n % 2 == 0:
    factors[2] = 0
    while n % 2 == 0:
      n /= 2
      factors[2] += 1

  for z in xrange(3, factor_limit, 2):
    if z > n:
      break

    if n % z == 0:
      factors[z] = 0
      while n % z == 0:
        n /= z
        factors[z] += 1

  if n > 1:
    factors[n] = 1

  return factors

def num_divs(prime_factors):
  '''
  calculate the number of integral factors of a number given
  its prime factorization

  the trick is that the number of integral factors is equal to the
  product of the exponents(+1) of the number's prime factorization
  '''
  powers = [power+1 for power in prime_factors.values()]
  prod = 1
  for power in powers:
    prod *= power
  return prod

n = 0
tri_n = 0
while True:
  tri_n += n + 1
  n += 1

  tri_factors = calc_prime_factors(tri_n)
  num_tri_divs = num_divs(tri_factors)
  if num_tri_divs > limit:
    print tri_n
    break
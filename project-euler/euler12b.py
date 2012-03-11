#!/usr/bin/env python2.7

'''
identify the first triangular number to have more than five hundred divisors

useful facts:
1. the nth triangular number is given by the formula for the series of
  naturals (thanks school-boy Gauss!), n*(n+1)/2
2. n, n+1 are relatively prime
3. the number of positive integral divisors of n is equal to the product
  of the incremented exponents of its prime factorization (that is,
  the product of the numbers arrived at by adding one to each exponent
  in the prime factorization)
'''

limit = 500

def gen_prime_factors(n):
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

def calc_num_divs(prime_factors):
  '''
  Calculate the number of integral factors of a number given
  its prime factorization by useful fact #3:

  the number of integral factors is equal to the
  product of the exponents(+1) of the number's prime factorization
  '''
  powers = [power+1 for power in prime_factors.values()]
  prod = 1
  for power in powers:
    prod *= power
  return prod

def combine_tri_factors(f1, f2):
  '''
  Combine factors of the two terms of a triangular number as stated in
  useful fact #1: the nth triangular number is n*(n+1)/2

  By extension of useful fact #2, that n & n+1 are coprime, we know that
  n & (n+1)/2 are coprime too so we can simply combine the dictionaries of
  factors without worrying about overwriting any entries
  '''
  f1.update(f2)
  return f1

def try_sol(n, factors):
  '''Checks number of divisors of a candidate & outputs true solution'''
  num_div = calc_num_divs(factors)
  if num_div > limit:
    print n*(n+1)/2
    exit()

'''
Determine the number of divisors of each triangular number
in blocks of nth, (n+1)th, and (n+2)th triangular numbers with
only four prime factorizations of relatively small numbers
by recourse to useful fact #1

the nth triangular number, normally expressed n*(n+1)/2, is rewritten to give:
nth triangular     = (n+1)(n/2)     = n(n+1)/2
(n+1)th triangular = (n+1)(n+2)/2
(n+2)th triangular = (n+2)/2*(n+3)  = (n+2)(n+3)/2
'''
n = 2
while True:
  half_n = gen_prime_factors(n/2)
  n_plus = gen_prime_factors(n+1)
  tri_n = combine_tri_factors(half_n, n_plus)
  try_sol(n, tri_n)

  next_half_n = gen_prime_factors((n+2) / 2)
  tri_n_plus = combine_tri_factors(n_plus, next_half_n)
  try_sol(n+1, tri_n_plus)

  next_n_plus = gen_prime_factors(n+3)
  tri_n_plus2 = combine_tri_factors(next_n_plus, next_half_n)
  try_sol(n+2, tri_n_plus2)

  n += 2
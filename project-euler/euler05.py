#!/usr/bin env python2.7

# find smallest number evenly divided by 1...20
# (by prime factorization)

k = 20

def is_prime(num):
  if num == 2: return True

  for factor in xrange(2, int(num**.5)):
    if num % factor == 0:
      return False

  return True

divisors = range(2,k+1)
primes = [x for x in divisors if is_prime(x)]

prime_factorization = {}

for d in divisors:
  for p in primes:
    if p > d:
      break

    print 'trying to factor ', p, ' out of ', d

    if d % p == 0:
      prev_power = prime_factorization.get(p, 0)

      power = 0
      while d > 1:
        d /= p
        power += 1

      prime_factorization[p] = max(power, prev_power)

prod = 1
print prime_factorization
for prime, power in prime_factorization.iteritems():
  prod *= prime**power

print prod

#!/usr/bin env python2.7

# identify the initial value < 1,000,000 for which
# the Collatz sequence is longest

# calculate the collatz sequence, recording number of terms generated
# memoize results for faster calculation of longer sequences
def collatz(n, lens):
  c = n
  terms = 1
  while c != 1:
    memo = lens.get(c, 0)
    if memo != 0:
      return memo

    if c % 2 == 0:
      c /= 2
    else:
      c = c*3 + 1

    terms += 1

  # memoize result
  lens[n] = terms
  return terms

collatz_lens = {}

max_n = 0
max_terms = 0
for n in range(1, 10**6):
  print n

  terms = collatz(n, collatz_lens)
  if terms > max_terms:
    max_n = n
    max_terms = terms

print 'collatz(', max_n, ') produces ', max_terms

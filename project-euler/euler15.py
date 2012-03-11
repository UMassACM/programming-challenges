#!`env python`

# problem 15: how many routes (without backtracking) are there
# through a 20x20 grid, proceeding from top-left to bottom-right

from math import factorial

# insight: the problem is actually asking how many permutations of
# 20 right and 20 down edges are there, or equivalently how many
# bit strings are there with 20 0s and 20 1s?

# the answer is n choose k, w/ n = 40 and k = 20, the problem of selecting
# the 10 bits to be 0 (or 1, equivalently)
n = 40
k = 20

# n choose k = n^k_falling / k! where n^k_falling is equal to the first
# k terms of n!
def choose(n, k):
  nCk = 1
  # calculate product of each n^k/k term
  for term in range(min(k, n-k)):
    nCk = nCk*(n - term)//(term+1)
  return nCk

print choose(n, k)
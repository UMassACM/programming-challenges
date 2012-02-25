#!/usr/bin env python2.7

# determine millionth permutation of the digits 0-9
count = 0

def permute(els):
  '''generate all permutations of elements by recursion'''
  els = [str(x) for x in els]
  return _permute(els, [])

def _permute(els, taken):
  '''recursively choose elements to build permutation tree, counting each
  permutation generated'''
  perms = []
  available = filter(lambda x: x not in taken, els)

  # base case: return the last available elements
  if len(available) == 1:
    global count
    count += 1
    print count

    if count == 10**6:
      print taken + available
      exit()

    return available

  # recursive case: pick each available element,
  # and
  for el in available:
    this_taken = taken[:]
    this_taken.append(el)

    for perm in _permute(els, this_taken):
      perms.append(el + ''.join(perm))

  return perms

permute(range(0,10))

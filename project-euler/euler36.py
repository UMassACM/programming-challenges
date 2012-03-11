#!/usr/bin env python2.7

# Find all binary/decimal palindromes less than one million

from math import log, ceil

def combinations(seq, k):
  # collect sequence elements for simple indexing
  pool = tuple(seq)
  n = len(pool)

  # indices for elements to include in combination, and 1st combination
  indices = range(k)
  yield tuple(pool[i] for i in indices)

  # generate all combinations...
  while 1:
    # ...until the last is made (consisting of the last k indices)
    for i in reversed(range(k)):
      if indices[i] != i + n - k:
        break
    else:
      return

    indices[i] += 1
    for j in range(i+1, k):
      indices[j] = indices[j-1] + 1
    yield tuple(pool[i] for i in indices)

def bit_combins(n, k):
  '''generates all possible n-bit strings w/ k 1s'''
  zeros = list('0' * n)
  bit_strs = []
  for ones in combinations(range(n), k):
    bit_str = zeros[:]
    for one in ones:
      bit_str[one] = '1'
    bit_strs.append(''.join(bit_str))
  return bit_strs


def is_palindrome(seq):
  '''determines if a sequence is a palindrome by matching from ends
  inward'''
  seq = str(seq)
  length = len(seq)

  depth = 0
  if length % 2 == 0:
    target = length / 2
    while seq[depth] == seq[-(depth+1)] and depth < target:
      depth += 1
    if depth == target:
      return True
  else:
    target = (length-1) / 2
    while seq[depth] == seq[-(depth+1)] and depth < target:
      depth += 1
    if depth == target:
      return True

  return False


palindromes = [('1', '1'), ('11', '3')]

limit = 10**6

# determine number of bits to express a million, and binary
# representation to know limits of computation
max_bits = int(ceil(log(limit, 2)))

# constraint of decimal/binary palindrome forces first and last
# bits to be 1, so we can generate all palindromes by reflecting
# a binary string between the two ends

palindrome_sum = 1 + 3

# for every bit string length...
for bit_len in range(1, (max_bits) / 2 + 1):
  # for every combination in numbers of zeros and ones...
  for num_0s in range(0, bit_len+1):
    # generate all half bit strings to reflect into a palindrome,
    # and assemble full bit pattern
    for bit_str in bit_combins(bit_len, bit_len - num_0s):
      bit_palin0 = '1' + bit_str + bit_str[-2::-1] + '1'
      bit_palin1 = '1' + bit_str + bit_str[::-1] + '1'
      dec_bit0 = int(bit_palin0, 2)
      dec_bit1 = int(bit_palin1, 2)

      # halt at limit
      if dec_bit0 > limit:
        break

      # record and add if palindrome in both bases
      if is_palindrome(dec_bit0):
        palindromes.append((bit_palin0, dec_bit0))
        palindrome_sum += dec_bit0
      if is_palindrome(dec_bit1):
        palindromes.append((bit_palin1, dec_bit1))
        palindrome_sum += dec_bit1
    else:
      continue
    break
  else:
    continue
  break

print palindromes
print palindrome_sum

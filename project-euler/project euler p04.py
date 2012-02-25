#!/usr/bin env python2.7

# determine the largest palindrome product of two 3-digit numbers

upper = 999
lower = 100
limit = (upper - lower) / 2

def is_palindrome(seq):
  '''
  determines if a sequence is a palindrome by matching from ends
  inward
  '''
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

upper = 999
lower = 100

max_palindrome = 0

low_term = upper
while low_term >= lower:
    high_term = upper
    while high_term >= low_term:
      if high_term*low_term <= max_palindrome:
        break

      if is_palindrome(high_term*low_term):
        max_palindrome = high_term*low_term

      high_term -= 1
    low_term -=1

print max_palindrome

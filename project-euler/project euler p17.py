#!/usr/bin env python2.7

# calculate the number of letters it takes to write out the numbers
# 1...1000 in British English style

ones = {
  0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
  6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'
}

ten_and_teens = {
  10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
  15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
  19: 'nineteen'
}

tens = {
  2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty',
  7: 'seventy', 8: 'eighty', 9: 'ninety'
}

def write_n(n):
  if n == 1000:
    return 'one thousand'
  if n == 0:
    return ones[0]

  written_n = ''
  has_hundreds = has_tens = False

  # hundreds
  if n / 100 > 0:
    written_n += "%s hundred" % ones[n / 100]
    has_hundreds = True
    n %= 100

  # tens: ten & teens
  if n / 10 == 1:
    if has_hundreds:
      written_n += ' and '
    written_n += ten_and_teens[n]
    return written_n

  # tens: regular tens
  if n / 10 > 1:
    if has_hundreds:
      written_n += ' and '
    written_n += tens[n / 10]
    has_tens = True

  n %= 10

  # ones
  if n > 0:
    if has_hundreds and not has_tens:
      written_n += ' and '
    elif has_tens:
      written_n += ' '
    written_n += ones[n]

  return written_n

char_sum = 0
for n in xrange(1, 1001):
  print write_n(n)
  print write_n(n).replace(' ', ''), len(write_n(n).replace(' ', ''))
  char_sum += len(write_n(n).replace(' ', ''))

print char_sum

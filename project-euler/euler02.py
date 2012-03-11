#!/usr/bin env python2.7

# calculate the sum of even-valued terms of the Fibonacci sequence
# for all such terms less than 4 million

max_term = 4 * 10**6

prev_term = 1
cur_term = 2

fib_sum = 0

while cur_term < max_term:
  if cur_term % 2 == 0:
    fib_sum += cur_term
    print 'added: ', cur_term

  cur_term += prev_term
  prev_term = cur_term - prev_term
  print 'current: ', cur_term
  print 'prevous: ', prev_term

print fib_sum

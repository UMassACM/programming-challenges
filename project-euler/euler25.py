#!/usr/bin env python2.7

# find the first term of the fibonacci sequence to have 1000 digits
# n.b. find the term subscript, not the value itself

def fibonacci(this_term, last_term):
  this_term += last_term
  last_term = this_term - last_term
  return this_term, last_term

this_fib = last_fib = 1
this_term = 2
while len(str(this_fib)) < 1000:
  print this_fib, last_fib
  this_fib, last_fib = fibonacci(this_fib, last_fib)
  this_term += 1

print this_term

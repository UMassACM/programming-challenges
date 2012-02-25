#!/usr/bin env python2.7

# determine the sum of all natural numbers <= 1000 that are
# multiples of 3 or 5
# done by summation of list comprehension
sum([i for i in range(1,1000) if i % 3 == 0 or i % 5 == 0])

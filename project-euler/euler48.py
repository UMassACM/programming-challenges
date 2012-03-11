#!/usr/bin/env python2.7

# calculate the last ten digits of the series 1^1 + 2^2 + ... + 1000^1000

series_end = 1000
series_sum = 0
for x in range(1, series_end+1):
  series_sum += x**x
print str(series_sum)[-10:]
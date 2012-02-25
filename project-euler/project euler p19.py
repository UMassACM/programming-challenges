#!/usr/bin env python2.7

# count how many Sundays fell on the first of a month during the 20th century
# (1 Jan 1901 - 31 Dec 2000)

def days_to_next_month(current_month, year):
  '''determine days to skip to go to first of each month'''
  # look up table for number of days in each month
  month_lens = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  days = month_lens[current_month]

  # leap years
  if current_month == 1 and year % 4 == 0:
    days += 1

  return days

# start from knowledge that 1 Jan 1900 was a Monday, i.e. beginning of
# year -1 was a Monday, so beginning weekday is no. of days in a year
# mod no. of weekdays

day = 365 % 7

num_sundays = 0
for year in range(1901, 2001):
  for month in range(0, 12):
    print year, month, day

    if day % 7 == 6:
      num_sundays += 1

    day += days_to_next_month(month, year)

print num_sundays

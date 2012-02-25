#!/usr/bin env python2.7

# read in names file, sort into alphabetical order, and then calculate and add
# "name scores" for each name =
# (sum of alphabetical order of each char * rank in list)

with open('data/names.txt', 'r') as f:
  name_data = f.read()

# parse and sort names
names = name_data.replace('"','').split(',')
sorted_names = sorted(names)

# calculate name score by converting chars of each name to
# ordinal position in alphabet, summing, and multiplying
# by rank in list
letter_offset = ord('A')

name_score_sum = 0
for idx, name in enumerate(sorted_names):
  name_sum = sum([ord(char)-letter_offset+1 for char in name])
  name_score_sum += name_sum * (idx+1)

print name_score_sum

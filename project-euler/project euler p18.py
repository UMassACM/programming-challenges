#!/usr/bin env python2.7

# problem 18: find the maximum sum of a path from the
# top of the triangle to the bottom

triangle ='\
75\n\
95 64\n\
17 47 82\n\
18 35 87 10\n\
20 04 82 47 65\n\
19 01 23 75 03 34\n\
88 02 77 73 07 63 67\n\
99 65 04 28 06 16 70 92\n\
41 41 26 56 83 40 80 70 33\n\
41 48 72 33 47 32 37 16 94 29\n\
53 71 44 65 25 43 91 52 97 51 14\n\
70 11 33 28 77 73 17 78 39 68 17 57\n\
91 71 52 38 17 14 91 43 58 50 27 29 48\n\
63 66 04 68 89 53 67 30 73 16 69 87 40 31\n\
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'

triangle = [[int(x) for x in line.split(' ')] for line in triangle.split('\n')]

route = [[0] * len(line) for line in triangle]
route[0][0] = triangle[0][0]

for line_idx, tri_line in enumerate(triangle[:-1]):
  for num_idx, tri_num in enumerate(tri_line):
    route_sum   = route[line_idx][num_idx]
    # print line_idx, num_idx, route_sum
    left_child  = route_sum + triangle[line_idx+1][num_idx]
    right_child = route_sum + triangle[line_idx+1][num_idx+1]

    if left_child > route[line_idx+1][num_idx]:
      route[line_idx+1][num_idx] = left_child
    if right_child > route[line_idx+1][num_idx+1]:
      route[line_idx+1][num_idx+1] = right_child

print max(route[-1])

#!/usr/bin env python2.7

# problem 67: find the maximum sum of a path from
# the top of the triangle to the bottom, with 100 total rows

triangle = []
with open('triangle.txt', 'r') as tri_file:
  for line in tri_file:
    triangle.append([int(x) for x in line.split(' ')])

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

#!/usr/bin env python2.7

# determine sum of diagonals of a square, clockwise spiral

# after inspecting the spiral, one can discern a pattern among the corners:
# top-right is n^2
# top-left is n^2 - n + 1
# bottom-left is n^2 -2n + 2
# bottom-right is n^2 -3n + 3
# where n is the length of a dimension of the spiral

spiral_size = 1001

diag_sum = 1
for spiral in range(3, spiral_size+1, 2):
  print spiral
  size_square = spiral**2

  corners = []
  corners.append(size_square)
  corners.append(size_square - spiral + 1)
  corners.append(size_square - 2*spiral + 2)
  corners.append(size_square - 3*spiral + 3)

  diag_sum += sum(corners)

print diag_sum

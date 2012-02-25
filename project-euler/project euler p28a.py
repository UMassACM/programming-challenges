#!/usr/bin env python2.7

# determine sum of diagonals of a square, clockwise spiral
# (note that direction does not matter)

# strategy is to unwind the spiral and treat it like a line
# each "ring" of the spiral has four members along the diagonals,
# and each corner is found by advancing by the right step size,
# starting at 2 and then adding 2 after each ring since the corners
# are now two more apart

spiral_size = 1001
num_els = spiral_size*2-1

diag_sum = 1
diag_num = 1
step = 2

print 'ring 0', '\n', '1'

for ring in range(1, num_els / 4 + 1):
  print 'ring', ring
  for corner in range(0, 4):
    diag_num += step
    print diag_num
    diag_sum += diag_num

  step += 2


print diag_sum

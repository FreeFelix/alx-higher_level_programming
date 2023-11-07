#!/usr/bin/python3

def pascal_triangle(n):
  if n <= 0:
    return []

  triangle = [[1]]
  for x in range(1, n):
    current_row = triangle[-1]
    new_row = [1]
    for y in range(1, x):
      new_row.append(current_row[y - 1] + current_row[y])
    new_row.append(1)
    triangle.append(new_row)

  return triangle

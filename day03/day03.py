from functools import reduce

input_file = 'input.txt'

def process_input():
  with open(input_file) as f:
      content = f.readlines()
  # creating a char array
  grid = [list(str(x.strip())) for x in content]

  return grid

def grid_search(grid, slopex, slopey):
  # a simple grid-search, but we modulus the x
  # coord for an "infinte" wrap around
  # ~ O(y) for y height/slopey
  # slopex is x jumps, slopey is y jumps
  x = 0
  y = 0
  len_x = len(grid[0])
  len_y = len(grid)
  count = 0

  while (x < len_x and y < len_y):
    if grid[y][x] == '#':
      count += 1
    x += slopex
    x = x % len_x
    y += slopey
  return count

def part_one(grid):
  # plugging in 3,1
  return grid_search(grid, 3, 1)

def part_two(grid, arr):
  # mapping each item in the slope tuple to the grid search result
  # then reduce them by multiplying to get final product
  # ~ O(n * ymax) for n tuples, ymax largest height/slopey
  applied = map(lambda x: grid_search(grid, x[0], x[1]), arr)
  return reduce(lambda x, y: x*y, applied)


def main():
  grid = process_input()
  p1 = part_one(grid)
  print("P1: you would hit {} trees".format(p1))
  p2_arr = [(1,1), (3,1), (5,1), (7,1), (1,2)]
  p2 = part_two(grid, p2_arr)
  print("P2: your product is {} trees".format(p2))

if __name__ == "__main__":
  main()

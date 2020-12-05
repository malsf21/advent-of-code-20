from functools import reduce

input_file = 'input.txt'

def process_input():
  with open(input_file) as f:
      content = f.readlines()
  grid = [x.strip() for x in content]

  return grid

def bin_mult(c):
  # useful tool that converts B/R to 1
  if c == 'B' or c == 'R':
    return 1
  return 0

def get_row(str):
  # get row by using base 2
  row = 0
  for i in range(7):
    row += bin_mult(str[i]) * 2**(6 - i)
  return row

def get_col(str):
  # get column by using base 2
  col = 0
  for i in range(3):
    col += bin_mult(str[i + 7]) * 2**(2 - i)
  return col


def part_one(tickets):
  # get the row and column of each seat; apply the formula
  # linear in number of tickets
  applied = map(lambda x: get_row(x) * 8 + get_col(x), tickets)
  return max(applied)

def get_bound_sum(n):
  return n * (n + 1)/2

def part_two(tickets):
  # not my proudest code (i wanted to compare the lower sum, upper sum)
  # but i ended up being lazy and sorting + linear scan. not great, i know.
  # nlogn in number of tickets
  applied = map(lambda x: get_row(x) * 8 + get_col(x), tickets)
  sort = sorted(applied)
  s = set(sort) # this is actually buggy?
  for i in range(sort[0], sort[-1]):
    if i not in s:
      return i


def main():
  tickets = process_input()
  p1 = part_one(tickets)
  print("P1: the largest ticket is {}".format(p1))
  p2 = part_two(tickets)
  print("P2: your ticket is {}".format(p2))

if __name__ == "__main__":
  main()

input_file = 'input.txt'

def process_input():
  with open(input_file) as f:
      content = f.readlines()
  # stripping whitespace
  stripped = [x.strip() for x in content]

  return stripped

def line_set_op(elements, op):
  # for each 'group' (separated by double whitespace),
  # creates a character set for each line;
  # maps the group into the set-op for each line's set
  # complexity is O(n + k*op) for n lines, k groups * op complexity
  join_and_collapse = []
  buffer = []
  for line in elements:
    if not line:
      join_and_collapse.append(op(*buffer))
      buffer = []
    else:
      buffer.append(set(line))
  join_and_collapse.append(op(*buffer))

  return join_and_collapse

def line_set_union(answers):
  # helper function for p1
  # note that union is linear in set length
  return line_set_op(answers, set.union)

def line_set_intersection(answers):
  # helper function for p2
  # note that intersection is avg min of set lengths, but worst-case
  # multiplicative in each set length
  return line_set_op(answers, set.intersection)

def part_one(answers):
  # union each batch of groups, then map them
  # into their length; return the cumulative sum
  # map is linear in groups, so overall time complexity
  # is same as line_set_union
  unioned = line_set_union(answers)
  applied = map(lambda x: len(x), unioned)
  return sum(applied)

def part_two(answers):
  # intersection each batch of groups, then map them
  # into their length; return the cumulative sum
  # map is linear in groups, so overall time complexity
  # is same as line_set_intersection
  intersectioned = line_set_intersection(answers)
  applied = map(lambda x: len(x), intersectioned)
  return sum(applied)

def main():
  answers = process_input()
  p1 = part_one(answers)
  print("P1: the total number of questions is {}".format(p1))
  p2 = part_two(answers)
  print("P2: the total number of questions is {}".format(p2))

if __name__ == "__main__":
  main()

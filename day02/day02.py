from collections import Counter

input_file = 'input.txt'

def process_input():
  with open(input_file) as f:
      content = f.readlines()

  # split on whitespace
  stripped_split = [x.strip().split() for x in content]

  # haha, this is pretty jank; list comprehension generates:
  # 1. lower bound of 'NUM-NUM', splitting on '-'
  # 2. upper bound of 'NUM-NUM'
  # 3. removes the ':' from the character
  # 4. the password
  final_list = [[int(x[0].split('-')[0]), int(x[0].split('-')[1]), x[1].replace(':',''), x[2]] for x in stripped_split]

  return final_list

def check_pw_freq(pw_entry):
  # create a counter of frequency in each character;
  # check if it fits bounds; ret 1 if it does, 0 if not
  lower, upper, cha, pw = pw_entry
  res = Counter(pw)
  if res[cha] >= lower and res[cha] <= upper:
    return 1
  return 0

def check_pw_xor(pw_entry):
  # the way this is worded sounds like an XOR
  # so let's XOR when they're equal
  lower, upper, cha, pw = pw_entry

  # subtract 1 because 1-index
  if (pw[lower - 1] == cha) != (pw[upper - 1] == cha):
    return 1
  return 0


def part_one(pw_list):
  # map each password to our check_pw_freq function
  # then sum up all the values
  return sum(map(check_pw_freq, pw_list))


def part_two(pw_list):
  # identical logic as above
  return sum(map(check_pw_xor, pw_list))

def main():
  pw_list = process_input()
  p1 = part_one(pw_list)
  print("P1: there are {} correct passwords".format(p1))
  p2 = part_two(pw_list)
  print("P2: there are {} correct passwords".format(p2))

if __name__ == "__main__":
  main()

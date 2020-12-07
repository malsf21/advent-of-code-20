input_file = 'input.txt'

def process_input():
  with open(input_file) as f:
      content = f.readlines()
  # stripping whitespace
  stripped = [x.strip() for x in content]

  return stripped

def build_rules(raw):
  # converts the line-by-line representation
  # into a dictionary, keyed by the bag (e.g. "mirrored black")
  # with each value being an array of tuples, (bag name, freq)
  # where each tuple corresponds with one type of bag it contains,
  # and has the bag name + the frequency
  # O(n * m), where n is the num of lines, and m is the avg number of bags
  # each bag contains
  rules = {}
  for line in raw:
    # first, splits into current bag and the bags it contains
    spl = line.split(" bags contain")
    current = spl[0]
    buffer = []
    if "no other bags" not in spl[1]:
      # now, split on the bags it contains
      inner = spl[1].split(",")
      for bag_str in inner:
        # a little ugly, but create the tuple described above
        bag = bag_str.split()
        buffer.append(("{} {}".format(bag[1], bag[2]), int(bag[0])))
    rules[current] = buffer
  return rules

# # for posterity - my failed attempt at a recursive search
# def recur_search(rules, search, current):
#   if len(rules[current]) == 0:
#     return 0
#   elif current == search:
#     return 1
#   else:
#     ans = 0
#     for bag in rules[current]:
#       ans += recur_search(rules, search, bag[0])
#     return ans

def part_one(rules, search):
  # not my favourite approach here, but basically a mark-and-sweep style
  # in each iteration of the while loop,
  #   loop through each type of bag
  #   if we haven't confirmed it contains our bag,
  #     check all of its bags, and see if we know any of them;
  #     if so, add it to our set of bags that contain search
  # repeat until one iteration adds no new bags to our known set
  # time complexity: pretty bad, but ~ O(n * t)
  # where n is number of bags, and t is the tree-depth of the
  # bag inheritance tree (approximates number of times while loop runs)
  ans = 0
  contained = set([search])
  diff = 1
  while diff > 0:
    diff = 0
    for bag in rules.keys():
      if bag not in contained:
        for inner in rules[bag]:
          if inner[0] in contained:
            contained.add(bag)
            diff += 1
            break

  # sub 1 because the bag itself doesn't count
  return len(contained) - 1

def count_nested_bags(rules, current):
  # simple recursive function that counts how many bags are contained
  # within one 'current' bag, including itself
  # one iteration has O(m) complexity with m average bags per bag
  # in total, expect to call it O(n * m * t) times, with n bags,
  # m avg bags, and t average tree-depth of bag tree
  if len(rules[current]) == 0:
    return 1
  else:
    # note the add 1 - we count ourselves
    return sum(map(lambda x: x[1] * count_nested_bags(rules, x[0]), rules[current])) + 1

def part_two(rules, search):
  # see above; subtract one since we don't count our original bag
  return count_nested_bags(rules, search) - 1

def main():
  raw = process_input()
  rules = build_rules(raw)
  p1 = part_one(rules, "shiny gold")
  print("P1: the total number of outer bags is {}".format(p1))
  p2 = part_two(rules, "shiny gold")
  print("P2: the total number of inner bags {}".format(p2))

if __name__ == "__main__":
  main()

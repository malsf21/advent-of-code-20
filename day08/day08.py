input_file = 'input.txt'

def process_input():
  with open(input_file) as f:
      content = f.readlines()
  # stripping whitespace
  stripped = [x.strip() for x in content]

  return stripped

def parse_instruction(current, accumulator, instruction, val):
  # helper that parses one line and does whatever we need to do
  # constant time
  if instruction == "jmp":
    current += int(val)
  else:
    if instruction == "acc":
      accumulator += int(val)
    current += 1
  return current,accumulator

def part_one(instructions):
  # relatively simple logical solution: just follow the IP
  # keep track of where we've visited; simulate the pointer and accum
  # includes a check for termination since we use this in part_two
  # ~ linear in number of lines
  visited = set()
  accumulator = 0
  current = 0
  while True:
    if current in visited or current == len(instructions):
      break
    else:
      visited.add(current)
      current, accumulator = parse_instruction(current, accumulator, instructions[current][0], instructions[current][1])
  return accumulator

def program_terminates(instructions):
  # helper that checks if the program terminates
  # basically the same thing as part_one, with slightly
  # diff return values
  visited = set()
  accumulator = 0
  current = 0
  while True:
    if current == len(instructions):
      return True
    elif current in visited:
      return False
    else:
      visited.add(current)
      current, accumulator = parse_instruction(current, accumulator, instructions[current][0], instructions[current][1])


def part_two(instructions):
  # a not-so-smart way of finding the answer
  # brute-force each flip, check if it terminates;
  # then, run part one
  # time complexity: very inefficient^TM
  for i in range(len(instructions)):
    line = instructions[i]
    if line[0] == "acc":
      continue
    else:
      fixed = "nop" if line[0] == "jmp" else "nop"
      nlist = instructions.copy()
      nlist[i] = [fixed, line[1]]
      if program_terminates(nlist):
        return part_one(nlist)

def main():
  raw = process_input()
  instructions = [line.split() for line in raw]
  p1 = part_one(instructions)
  print("P1: the value of the accumulator is {}".format(p1))
  p2 = part_two(instructions)
  print("P2: the value of the accumulator is {}".format(p2))

if __name__ == "__main__":
  main()

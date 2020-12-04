import string
required_fields= {
  "byr",
  "iyr",
  "eyr",
  "hgt",
  "hcl",
  "ecl",
  "pid"
}

eye_colors = {
  "amb",
  "blu",
  "brn",
  "gry",
  "grn",
  "hzl",
  "oth"
}

hex_digits = {
  '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'
}

input_file = 'input.txt'

def process_input():
  with open(input_file) as f:
      content = f.readlines()
  # creating a char array
  stripped = [x.strip() for x in content]
  join_and_collapse = []
  buffer = dict()
  for line in stripped:
    if not line:
      join_and_collapse.append(buffer)
      buffer = dict()
    else:
      for item in line.split():
        kv = item.split(':')
        buffer[kv[0]] = kv[1]
  join_and_collapse.append(buffer)

  return join_and_collapse

# just checks if the required keys are a subset of the
# total passport keys
# is it constant/linear? idk
def weak_check(passport):
  if required_fields.issubset(set(passport.keys())):
    return 1
  return 0

def within_bounds(val, l, u):
  return val.isdigit() and int(val) >= l and int(val) <= u

def field_check(field, value):
  # ugly switch-case
  # nothing out of ordinary, basically implementing
  # the spec
  if field == "byr":
    return within_bounds(value, 1920, 2002)
  elif field == "iyr":
    return within_bounds(value, 2010, 2020)
  elif field == "eyr":
    return within_bounds(value, 2020, 2030)
  elif field == "hgt":
    if value[-2:] == "in" or value[-2:] == "cm":
      val = value[:-2]
      if value[-2:] == "cm":
        return within_bounds(val, 150, 193)
      else:
        return within_bounds(val, 59, 76)
    else:
      return False
  elif field == "hcl":
    return (value[0] == '#' and len(value) == 7 and all(c in hex_digits for c in value[1:]))
  elif field == "ecl":
    return value in eye_colors
  elif field == "pid":
    return len(value) == 9 and value.isdigit()
  elif field == "cid":
    return True
  else:
    print("matt, you made a mistake")

def strong_check(passport):
  # runs both the weak check and field check on each field
  # linear in num of required fields
  if weak_check(passport) and all(field_check(key, passport[key]) for key in passport.keys()):
    return 1
  return 0


def part_one(passports):
  # just maps each passport to valid/invalid and sums
  # linear in passports, unsure of multiplier
  applied = map(lambda x: weak_check(x), passports)
  return sum(applied)

def part_two(passports):
  # similar maps each passport to valid/invalid and sums
  # linear in passports, scales linearly w/ num of checks
  # some of the checks are themselves linear in length of field
  # buttttt all fields are constant-defined so that's good
  applied = map(lambda x: strong_check(x), passports)
  return sum(applied)

def main():
  passports = process_input()
  p1 = part_one(passports)
  print("P1: there are {} valid passports".format(p1))
  p2 = part_two(passports)
  print("P2: there are {} valid passports".format(p2))

if __name__ == "__main__":
  main()

input_file = 'input.txt'
target_num = 2020

def process_input():
  with open(input_file) as f:
      content = f.readlines()
  price_list = [int(x.strip()) for x in content]

  return sorted(price_list)

def part_one(prices, target):
  # now, this just becomes two-sum for 2020, and then we output the product
  # ~ linear in prices
  head = 0
  tail = len(prices) - 1
  for _ in range(len(prices)):
    result = prices[head] + prices[tail]
    if result == target:
      return (prices[head], prices[tail])
    elif result < target:
      head += 1
    else:
      tail -= 1
  return None
  # print("hmmmm... this didn't work. matt clearly made a mistake.")

def part_two(prices):
  # haven't done 3-sum in a while, but a seemingly-bad
  # solution is linear search the first term, then 2-sum the remaining two
  # ~ n^2 in prices (big sad)
  for head in range(len(prices)):
    attempt = part_one(prices[head + 1:], target_num - prices[head])
    if attempt != None:
      return (prices[head], attempt[0], attempt[1])
  return None





def main():
  prices = process_input()
  p1 = part_one(prices, target_num)
  print("P1: the two prices are {} and {}; their product is {}".format(p1[0], p1[1], p1[0] * p1[1]))
  p2 = part_two(prices)
  print("P2: the three prices are {}, {}, and {}; their product is {}".format(p2[0], p2[1], p2[2], p2[0] * p2[1] * p2[2]))



if __name__ == "__main__":
  main()

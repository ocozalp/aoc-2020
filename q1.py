def solve():
  with open('input/q1.txt', 'r') as f:
    lines = list(map(int, map(lambda s: s[:-1], f.readlines())))

  print('Answer 1:', solve1(lines[:]))
  print('Answer 2:', solve2(lines[:]))

def solve1(numbers):
  nums = set(numbers)
  for number in numbers:
    if 2020 - number in nums:
      return number * (2020 - number)


def solve2(numbers):
  muls = dict()
  for i in range(len(numbers)):
    num = numbers[i]
    if 2020 - num in muls:
      return num * muls[2020 - num]

    for j in range(i):
      s = numbers[i] + numbers[j]
      m = numbers[i] * numbers[j]
      muls[s] = m

solve()

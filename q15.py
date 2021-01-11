from collections import defaultdict


def solve():
  with open('input/q15.txt', 'r') as f:
    lines = [line[:-1] for line in f.readlines()]

  print('Answer 1:', solve1(lines[:]))
  print('Answer 2:', solve2(lines[:]))


def solve1(lines, iter_count=2020):
  nums = list(map(int, lines[0].split(',')))
  last_turns = dict()
  for i, num in enumerate(nums):
    last_turns[num] = (i, -1)

  current_num = nums[-1]
  for turn in range(len(nums), iter_count):
    if current_num not in last_turns:
      last_turns[current_num] = (turn, -1)
    else:
      lt = last_turns[current_num]
      if lt[1] == -1:
        current_num = 0
      else:
        current_num = lt[0] - lt[1]

      if current_num in last_turns:
        lt = last_turns[current_num]
        last_turns[current_num] = (turn, lt[0])
      else:
        last_turns[current_num] = (turn, -1)

  return current_num


def solve2(lines):
  return solve1(lines, 30000000)


solve()

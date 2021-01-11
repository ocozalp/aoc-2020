from collections import defaultdict


def solve():
  with open('input/q10.txt', 'r') as f:
    lines = [int(line[:-1]) for line in f.readlines()]

  print('Answer 1:', solve1(lines[:]))
  print('Answer 2:', solve2(lines[:]))


def solve1(lines):
  lines.sort()

  current = 0
  diffs = [0] * 4
  for i, num in enumerate(lines):
    diff = num - current
    if diff > 3:
      return None
    diffs[diff] += 1
    current = num
  return diffs[1] * (diffs[3]+1)


def solve2(lines):
  lines.sort()
  last = max(lines) + 3
  ways_to_go = defaultdict(int)
  lines.append(last)
  lines.insert(0, 0)

  ways_to_go[0] = 1
  for curr in lines:
    w = ways_to_go[curr]
    for j in range(1, 4):
      ways_to_go[curr + j] += w

  return ways_to_go[last]


solve()

from collections import defaultdict


def solve():
  with open('input/q6.txt', 'r') as f:
    lines = list(map(lambda s: s[:-1], f.readlines()))

  print('Answer 1:', solve1(lines[:]))
  print('Answer 2:', solve2(lines[:]))

def solve1(lines):
  current = set()
  res = 0
  for line in lines:
    if line == '':
      res += len(current)
      current = set()
    else:
      current |= set(line)
  res += len(current)
  return res


def solve2(lines):
  current = defaultdict(int)
  currcount = 0
  res = 0
  for line in lines:
    if line == '':
      if currcount != 0:
        for a in current:
          if current[a] == currcount:
            res += 1
        current = defaultdict(int)
        currcount = 0
    else:
      for c in line:
        current[c] += 1
      currcount += 1
  for a in current:
    if current[a] == currcount:
      res += 1
  return res

solve()

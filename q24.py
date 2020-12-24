from collections import defaultdict


vec = {
  'e': [1, 0],
  'se': [0.5, 0.5],
  'sw': [-0.5, 0.5],
  'w': [-1, 0],
  'nw': [-0.5, -0.5],
  'ne': [0.5, -0.5]
}


def solve():
  with open('input/in.txt', 'r') as f:
    lines = [line[:-1] for line in f.readlines()]

  print('Answer 1:', solve1(lines[:]))
  print('Answer 2:', solve2(lines[:]))


def get_blacks(lines):
  flips = defaultdict(int)
  for line in lines:
    i = 0
    x = 0
    y = 0
    while i < len(line):
      if line[i] == 'e' or line[i] == 'w':
        key = line[i: i + 1]
      else:
        key = line[i: i + 2]

      v = vec[key]
      x += v[0]
      y += v[1]
      i += len(key)
    flips[(x, y)] += 1
  return {k for k, v in flips.items() if v % 2 == 1}


def solve1(lines):
  return len(get_blacks(lines))


def solve2(lines):
  blacks = get_blacks(lines)

  for _ in range(100):
    whites = defaultdict(int)
    for b in blacks:
      ne = get_n(b[0], b[1]) - blacks
      for n in ne:
        whites[n] += 1

    blacks2 = set()
    for b in blacks:
      ne = get_n(b[0], b[1]) & blacks
      if 1 <= len(ne) <= 2:
        blacks2.add(b)

    blacks2 |= {k for k, v in whites.items() if v == 2}
    blacks = blacks2
  return len(blacks)


def get_n(x, y):
  return {(x + v[0], y + v[1]) for v in vec.values()}


solve()

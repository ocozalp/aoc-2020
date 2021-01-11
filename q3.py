def solve():
  with open('input/q3.txt', 'r') as f:
    lines = list(map(lambda s: s[:-1], f.readlines()))

  print('Answer 1:', solve1(lines[:]))
  print('Answer 2:', solve2(lines[:]))


def count_trees(lines, c, r):
  col = 0
  cols = len(lines[0])
  count = 0
  for row in range(r, len(lines), r):
    col = (col + c) % cols
    if lines[row][col] == '#':
      count += 1
  return count


def solve1(lines):
  return count_trees(lines, 3, 1)


def solve2(lines):
  calc = lambda c, r: count_trees(lines, c, r)
  return calc(1, 1) * calc(3, 1) * calc(5, 1) * calc(7, 1) * calc(1, 2)

solve()

from collections import defaultdict

vecs = [
  [-1,-1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]
]

def solve():
  with open('input/in.txt', 'r') as f:
    lines = [line[:-1] for line in f.readlines()]

  lines = list(map(list, lines))
  print('Answer 1:', solve1(lines))
  print('Answer 2:', solve2(lines[:]))


def copy(l):
  return list(map(list, l))


def solve1(lines):
  changed = True
  current = copy(lines)
  newlines = copy(lines)

  while changed:
    changed = False
    newlines, current = current, newlines

    for i, line in enumerate(current):
      for j, c in enumerate(line):
        if c == '.':
          continue
        no, o = count_neigh(current, i, j)
        if c == '#':
          if o >= 4:
            changed = True
            newlines[i][j] = 'L'
          else:
            newlines[i][j] = '#'
        elif c == 'L':
          if o == 0:
            changed = True
            newlines[i][j] = '#'
          else:
            newlines[i][j] = 'L'
  count = 0
  for line in newlines:
    count += len([c for c in line if c == '#'])
  return count


def count_neigh(lines, i, j):
  no = 0
  o = 0
  for vec in vecs:
    r = i+vec[0]
    c = j+vec[1]
    if 0 <= r < len(lines) and 0 <= c < len(lines[r]):
      if lines[r][c] == '#':
        o += 1
      elif lines[r][c] == 'L':
        no += 1
  return no, o


def solve2(lines):
  changed = True
  current = copy(lines)
  newlines = copy(lines)

  while changed:
    changed = False
    newlines, current = current, newlines

    for i, line in enumerate(current):
      for j, c in enumerate(line):
        if c == '.':
          continue
        no, o = count_neigh2(current, i, j)
        if c == '#':
          if o >= 5:
            changed = True
            newlines[i][j] = 'L'
          else:
            newlines[i][j] = '#'
        elif c == 'L':
          if o == 0:
            changed = True
            newlines[i][j] = '#'
          else:
            newlines[i][j] = 'L'

  count = 0
  for line in newlines:
    count += len([c for c in line if c == '#'])
  return count


def count_neigh2(lines, i, j):
  no = 0
  o = 0
  for vec in vecs:
    r = i+vec[0]
    c = j+vec[1]
    while 0 <= r < len(lines) and 0 <= c < len(lines[r]):
      if lines[r][c] == '#':
        o += 1
        break
      elif lines[r][c] == 'L':
        no += 1
        break

      r += vec[0]
      c += vec[1]
  return no, o


solve()

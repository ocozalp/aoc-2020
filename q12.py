from collections import defaultdict


vecs = [
  [1, 0], [0, -1], [-1,0], [0, 1]
]

vec_i = {
  'E': 0,
  'S': 1,
  'W': 2,
  'N': 3
}


def solve():
  with open('input/in.txt', 'r') as f:
    lines = [line[:-1] for line in f.readlines()]

  print('Answer 1:', solve1(lines[:]))
  print('Answer 2:', solve2(lines[:]))


def solve1(lines):
  d = 0
  pos = [0, 0]
  for line in lines:
    dd = line[0]
    num = int(line[1:])
    if dd == 'F':
      pos[0] += num * vecs[d][0]
      pos[1] += num * vecs[d][1]
    elif dd == 'R':
      d = (d + num / 90) % 4
    elif dd == 'L':
      d = (d + 3 * (num / 90)) % 4
    else:
      ind = vec_i[dd]
      pos[0] += num * vecs[ind][0]
      pos[1] += num * vecs[ind][1]

  return abs(pos[0]) + abs(pos[1])


def solve2(lines):
  wp = [10, 1]
  pos = [0, 0]

  for line in lines:
    dd = line[0]
    num = int(line[1:])
    if dd == 'F':
      pos[0] += num * wp[0]
      pos[1] += num * wp[1]
    elif dd == 'R':
      for _ in range(num/90):
        wp[0], wp[1] = wp[1], -wp[0]
    elif dd == 'L':
      for _ in range(num/90):
        wp[0], wp[1] = -wp[1], wp[0]
    else:
      ind = vec_i[dd]
      wp[0] += num * vecs[ind][0]
      wp[1] += num * vecs[ind][1]

  return abs(pos[0]) + abs(pos[1])


solve()

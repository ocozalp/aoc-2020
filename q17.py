from collections import defaultdict

def solve():
  with open('input/q17.txt', 'r') as f:
    lines = [line[:-1] for line in f.readlines()]

  print('Answer 1:', solve1(lines[:]))
  print('Answer 2:', solve2(lines[:]))


def solve1(lines):
  states = dict()
  for i in range(len(lines)):
    for j in range(len(lines[i])):
      states[(i,j,0)] = lines[i][j] == '#'

  l = len(lines)

  for it in range(1, 7):
    states2 = dict()
    for k in states:
      states2[k] = states[k]

    for i in range(-it, l+it+1):
      for j in range(-it, l+it+1):
        for z in range(-it, l+it+1):
          key = (i, j, z)
          ns = get_n(i, j, z)
          is_active = key in states and states[key]

          active_n = len([n for n in ns if n in states and states[n]])
          if is_active:
            states2[key] = 2 <= active_n <= 3
          else:
            states2[key] = active_n == 3

    states = states2


  return len([k for k in states if states[k]])

def solve2(lines):
  states = dict()
  for i in range(len(lines)):
    for j in range(len(lines[i])):
      if lines[i][j] == '#':
        states[(i, j, 0, 0)] = True
      else:
        states[(i, j, 0, 0)] = False

  l = len(lines)

  def st_active(states, key):
    return key in states and states[key]

  for it in range(1, 7):
    states2 = dict()
    for ki in states:
      states2[ki] = states[ki]

    for i in range(-it, l+it+1):
      for j in range(-it, l+it+1):
        for z in range(-it, l+it+1):
          for k in range(-it, l+it+1):
            key = (i, j, z, k)
            ns = get_n4(i, j, z, k)

            is_active = st_active(states, key)

            active_n = len([n for n in ns if st_active(states, n)])

            if is_active:
              states2[key] = 2 <= active_n <= 3
            else:
              states2[key] = active_n == 3
    states = states2

  return len([k for k in states if states[k]])


def get_n4(i, j, z, k):
  result = list()
  for di in range(-1, 2):
    ii = i+di
    for dj in range(-1, 2):
      jj = j+dj
      for dz in range(-1, 2):
        zz = z + dz
        for dk in range(-1, 2):
          kk = k + dk
          if ii == i and  jj == j and zz == z and kk == k:
            continue
          result.append((ii, jj, zz, kk))

  return result


def get_n(i, j, z):
  result = list()
  for di in range(-1, 2):
    ii = i+di
    for dj in range(-1, 2):
      jj = j+dj
      for dz in range(-1, 2):
        zz = z + dz
        if ii == i and  jj == j and zz == z:
          continue
        result.append((ii, jj, zz))

  return result

solve()

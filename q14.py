from collections import defaultdict

def solve():
  with open('input/q14.txt', 'r') as f:
    lines = [line[:-1] for line in f.readlines()]

  print('Answer 1:', solve1(lines[:]))
  print('Answer 2:', solve2(lines[:]))


def solve1(lines):
  mem = dict()
  for i in range(len(lines)):
    line = lines[i]
    if line[:4] == 'mask':
      mask = line.split('=')[1].strip()
    else:
      idx = line.find(']')
      memidx = int(line[4:idx])

      val = int(line.split('=')[1].strip())

      assigned_val = get_assigned_val(mask, val)
      mem[memidx] = assigned_val

  return sum(mem.values())


def get_assigned_val(mask, val):
  result = 0
  v = val
  mul = 1
  for i in range(len(mask)):
    c = mask[-i-1]
    val_bit_set = (v % 2 == 1)

    if c == '1' or  (c == 'X' and val_bit_set):
      result += mul
    mul *= 2
    v /= 2
  return result


def solve2(lines):
  mem = dict()
  res = 0
  for i in range(len(lines)):
    line = lines[i]
    if line[:4] == 'mask':
      mask = line.split('=')[1].strip()
    else:
      idx = line.find(']')
      memidx = int(line[4:idx])
      val = int(line.split('=')[1].strip())

      assign_vals(mem, mask, memidx, val)

  for k in mem:
    res += mem[k]
  return res


def assign_vals(mem, mask, memidx, val):
  res = []
  v = memidx
  for i in range(len(mask)):
    c = mask[-i-1]
    if c == 'X':
      res.append('X')
    elif c == '1':
      res.append('1')
    else:
      if v % 2 == 1:
        res.append('1')
      else:
        res.append('0')
    v /= 2
  res = list(reversed(res))

  front = [[]]
  for c in res:
    if c == 'X':
      front2 = list()
      for a in front:
        front2.append(a[:] + ['1'])
        front2.append(a[:] + ['0'])
      front = front2
    else:
      for a in front:
        a.append(c)

  for f in front:
    f = list(reversed(f))
    a = toint(f)
    mem[a] = val


def toint(arr):
  res = 0
  m = 1
  for i in range(len(arr)):
    v = 0
    if arr[-i - 1] == '1':
      v = 1
    res += v * m
    m *= 2
  return res


solve()

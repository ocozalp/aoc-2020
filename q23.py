from collections import defaultdict


def solve():
  with open('input/q23.txt', 'r') as f:
    lines = [line[:-1] for line in f.readlines()]

  print('Answer 1:', solve1(lines[:]))
  print('Answer 2:', solve2(lines[:]))


def solve1(lines):
  sample = lines[0]
  current = list(sample)
  current_index = 0
  for _ in range(100):
    to_be_removed = list()
    for j in range(1, 4):
      jj = (current_index + j) % len(current)
      to_be_removed.append(current[jj])

    s = set(to_be_removed)
    num = current[current_index]
    others = [(n, idx) for idx, n in enumerate(current) if n not in s and n != num]
    smaller = [n for n in others if n[0] < num]

    if smaller:
      smaller.sort()
      idx = smaller[-1][1]
    else:
      others.sort()
      idx = others[-1][1]

    target = current[idx]
    nxt = (current_index + 1) % len(current)
    while True:
      nnxt = (nxt + 3) % len(current)
      current[nxt] = current[nnxt]
      if current[nxt] == target:
        break
      nxt = (nxt+1)%len(current)

    for i in range(1, 4):
      nxt = (nxt + 1) % len(current)
      current[nxt] = to_be_removed[i - 1]

    current_index = (current_index + 1) % len(current)

  res = ''.join(current)
  l = len(current)
  res = res + res
  idx = res.find('1')
  return res[idx+1:idx+l]


def solve2(lines):
  from itertools import chain
  l = 1000000
  iter_count = 10000000
  sample = lines[0]
  head = None
  prev = None

  # create linked list
  llmap = dict()
  for i in chain(map(int, list(sample)), range(len(sample)+1, l+1)):
    node = [i, None]
    if head is not None:
      prev[1] = node
    else:
      head = node
    llmap[i] = node
    prev = node
  prev[1] = head

  current_node = head
  for _ in range(iter_count):
    target_num = current_node[0]

    found_target = False
    while not found_target:
      target_num -= 1
      if target_num == 0:
        target_num = l

      s_start = current_node[1]
      found = False
      for _ in range(3):
        if s_start[0] == target_num:
          found = True
          break
        s_start = s_start[1]
      found_target = not found

    dest_node = llmap[target_num]

    rem_start = current_node[1]
    rem_end = rem_start
    for _ in range(2):
      rem_end = rem_end[1]

    # isolate 3 numbers
    t = rem_end[1]
    current_node[1] = t
    rem_end[1] = None

    dest_next = dest_node[1]

    dest_node[1] = rem_start
    rem_end[1] = dest_next

    current_node = current_node[1]

  one_node = llmap[1]
  res = one_node[1][0] * one_node[1][1][0]
  return res


solve()

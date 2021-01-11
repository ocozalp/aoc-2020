from collections import defaultdict


def solve():
  with open('input/q8.txt', 'r') as f:
    lines = [line[:-1] for line in f.readlines()]

  print('Answer 1:', solve1(lines[:]))
  print('Answer 2:', solve2(lines[:]))


def solve1(lines):
  graph = [-1] * len(lines)
  for i, line in enumerate(lines):
    cmd, val = line.split(' ')
    if cmd == 'nop':
      graph[i] = (i + 1, 0)
    elif cmd == 'jmp':
      graph[i] = (i + int(val), 0)
    else:
      graph[i] = (i + 1, int(val))

  visited = set()
  current = 0
  acc = 0
  while current not in visited:
    visited.add(current)
    nxt, a = graph[current]
    acc += a
    current = nxt
  return acc


def solve2(lines):
  graph = [-1] * len(lines)
  for i, line in enumerate(lines):
    cmd, val = line.split(' ')
    if cmd == 'nop':
      graph[i] = (i + 1, 0, i + int(val))
    elif cmd == 'jmp':
      graph[i] = (i + int(val), 0, i + 1)
    else:
      graph[i] = (i + 1, int(val), None)

  current = 0
  visited = set()
  loop = list()
  acc = 0
  while current not in visited:
    visited.add(current)
    loop.append((current, acc))
    nxt, a, _ = graph[current]
    acc += a
    current = nxt

  for i in range(len(loop)-1, -1, -1):
    n, current_acc = loop[i]
    nxt, acc, a_next = graph[n]
    if a_next is not None:
      aa = path(a_next, len(lines) - 1, graph)
      if aa is not None:
        return aa + current_acc


def path(start, target, graph):
  visited = set()
  current = start
  acc = 0
  while current not in visited:
    if current > target:
      return acc
    nxt, a, _ = graph[current]
    visited.add(current)
    if nxt == target:
      return acc + a
    acc += a
    current = nxt


solve()

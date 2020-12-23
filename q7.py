from collections import defaultdict


def solve():
  with open('input/in.txt', 'r') as f:
    lines = list(map(lambda s: s[:-1], f.readlines()))

  print('Answer 1:', solve1(lines[:]))
  print('Answer 2:', solve2(lines[:]))


def solve1(lines):
  graph = defaultdict(set)

  for line in lines:
    tokens = line.split(' ')
    f = (tokens[0], tokens[1])
    for i in range(4, len(tokens), 4):
      t = (tokens[i + 1], tokens[i + 2])
      graph[t].add(f)

  return traverse(graph, ('shiny', 'gold'))


def traverse(graph, node):
  frontier = [node]
  visited = set()

  while frontier:
    current = frontier.pop()
    if current in visited:
      continue
    visited.add(current)

    for n in graph[current]:
      frontier.append(n)

  return len(visited)-1


def solve2(lines):
  graph = defaultdict(set)

  for line in lines:
    tokens = line.split(' ')
    f = (tokens[0], tokens[1])
    for i in range(4, len(tokens), 4):
      t = (tokens[i + 1], tokens[i + 2])
      val = int('0' if tokens[i] == 'no' else tokens[i])
      if val != 0:
        graph[f].add((t, val))

  return traverse2(graph, ('shiny', 'gold')) - 1


def traverse2(graph, node):
  res = 1
  for n in graph[node]:
    res += n[1] * traverse2(graph, n[0])
  return res

solve()

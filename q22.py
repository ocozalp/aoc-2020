from collections import defaultdict


def solve():
  with open('input/q22.txt', 'r') as f:
    lines = [line[:-1] for line in f.readlines()]

  print('Answer 1:', solve1(lines[:]))
  print('Answer 2:', solve2(lines[:]))


def solve1(lines):
  player1 = list()
  player2 = list()
  i = 1
  while lines[i] != '':
    player1.append(int(lines[i]))
    i += 1

  i+=1
  for line in lines[i + 1 :]:
    player2.append(int(line))

  while len(player1) > 0 and len(player2) > 0:
    c1 = player1.pop(0)
    c2 = player2.pop(0)

    if c1 > c2:
      player1.append(max(c1, c2))
      player1.append(min(c1, c2))
    else:
      player2.append(max(c1, c2))
      player2.append(min(c1, c2))

  res = 0
  l = player1
  if len(player1) == 0:
    l = player2
  for i in range(len(l)):
    res += (i + 1) * l[-i-1]

  return res


def play(player1, player2):
  visited = set()

  while len(player1) > 0 and len(player2) > 0:
    k = (tuple(player1), tuple(player2))
    if k in visited:
      return [1], []
    visited.add(k)

    c1 = player1.pop(0)
    c2 = player2.pop(0)

    if len(player1) >= c1 and len(player2) >= c2:
      p1, p2 = play(player1[:c1], player2[:c2])
      p1_winner = len(p1) > 0
    else:
      p1_winner = c1 > c2

    if p1_winner:
      player1.append(c1)
      player1.append(c2)
    else:
      player2.append(c2)
      player2.append(c1)

  return player1, player2


def solve2(lines):
  player1 = list()
  player2 = list()
  i = 1
  while lines[i] != '':
    player1.append(int(lines[i]))
    i += 1

  i+=1
  for line in lines[i + 1 :]:
    player2.append(int(line))

  player1, player2 = play(player1[:], player2[:])

  res = 0
  l = player1
  if len(player1) == 0:
    l = player2
  for i in range(len(l)):
    res += (i + 1) * l[-i-1]

  return res


solve()

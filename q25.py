from collections import defaultdict


def solve():
  with open('input/in.txt', 'r') as f:
    lines = [line[:-1] for line in f.readlines()]

  print('Answer 1:', solve1(lines[:]))


def solve1(lines):
  card = int(lines[0])
  door = int(lines[1])

  count = calc(7, card)
  count2 = calc(7, door)

  val = calc2(card, count2)
  val2 = calc2(door, count)

  assert val == val2
  return val


def calc2(snum, count):
  val = 1
  for _ in range(count):
    val *= snum
    val = val % 20201227
  return val


def calc(snum, target):
  count = 0
  val = 1
  while True:
    count += 1
    val *= snum
    val = val % 20201227
    if val == target:
      break
  return count


solve()

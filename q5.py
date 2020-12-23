def solve():
  with open('input/in.txt', 'r') as f:
    lines = list(map(lambda s: s[:-1], f.readlines()))

  print('Answer 1:', solve1(lines[:]))
  print('Answer 2:', solve2(lines[:]))


def solve1(lines):
  res = max(map(calculate_seat_id, lines))
  return res

def solve2(lines):
  tickets = set(map(calculate_seat_id, lines))

  res = -1
  # 2^3 - (2^10 - 8)
  for num in range(8, 1016):
    if num not in tickets and num - 1 in tickets and num + 1 in tickets:
      res = num
  return res

def calculate_seat_id(line):
  res = 0
  for c in line:
    val = 1 if c == 'B' or c == 'R' else 0
    res = res * 2 + val
  return res

solve()

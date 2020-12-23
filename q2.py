def solve():
  with open('input/in.txt', 'r') as f:
    commands = list(map(convert_command, map(lambda s: s[:-1], f.readlines())))

  print('Answer 1:', solve1(commands))
  print('Answer 2:', solve2(commands))


def solve1(commands):
  result = 0
  for command in commands:
    c = command[2]
    count = len([_c for _c in command[3] if _c == c])
    if command[0] <= count <= command[1]:
      result += 1
  return result


def solve2(commands):
  result = 0
  for command in commands:
    c = command[2]
    txt = command[3]
    if bool(txt[command[0]-1] == c) ^ bool(txt[command[1]-1] == c):
      result += 1
  return result


def convert_command(line):
  idx = line.find(':')
  text = line[idx + 1 :].strip()
  constraint = line[: idx]
  c = constraint[-1]
  _min, _max = map(int, constraint[:-2].strip().split('-'))
  return (_min, _max, c, text)

solve()

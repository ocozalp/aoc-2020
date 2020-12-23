def solve():
  with open('input/in.txt', 'r') as f:
    lines = list(map(lambda s: s[:-1], f.readlines()))

  print('Answer 1:', solve1(lines[:]))
  print('Answer 2:', solve2(lines[:]))


def solve1(lines):
  fields = set()
  res = 0
  for line in lines:
    if line.strip() == '':
      if len(fields) == 8 or (len(fields) == 7 and 'cid' not in fields):
        res += 1
      fields = set()

    else:
      tokens = line.split(' ')
      for token in tokens:
        idx = token.find(':')
        if len(token[:idx]) > 0:
          fields.add(token[:idx])
  return res


def solve2(lines):
  fields = set()
  res = 0
  for line in lines:
    if line.strip() == '':
      if len(fields) == 8 or (len(fields) == 7 and 'cid' not in fields):
        res += 1
      fields = set()
    else:
      tokens = line.split(' ')
      for token in tokens:
        idx = token.find(':')
        if len(token[:idx]) > 0:
          key = token[:idx]
          value = token[idx + 1 :]
          if key == 'byr':
            if len(value) == 4 and isnumeric(value):
              vv = int(value)
              if 1920 <= vv <=2002:
                fields.add(key)
          elif key == 'iyr':
            if len(value) == 4 and isnumeric(value):
                vv = int(value)
                if 2010 <= vv <=2020:
                  fields.add(key)
          elif key == 'eyr':
            if len(value) == 4 and isnumeric(value):
                vv = int(value)
                if 2020 <= vv <=2030:
                  fields.add(key)
          elif key == 'cid':
            fields.add(key)
          elif key == 'pid':
            if len(value) == 9 and isnumeric(value):
              fields.add(key)
          elif key == 'ecl':
            if value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
              fields.add(key)
          elif key == 'hcl':
            if len(value) == 7 and value[0] == '#':
              try:
                int(value[1:], 16)
                fields.add(key)
              except Exception:
                pass
          elif key == 'hgt':
            if value[-2:] == 'cm':
              vv = value[:-2]
              if isnumeric(vv) and 150 <= int(vv) <= 193:
                fields.add(key)
            elif value[-2:] == 'in':
              vv = value[:-2]
              if isnumeric(vv) and 59 <= int(vv) <= 76:
                fields.add(key)
  return res

def isnumeric(s):
  return len(set(s) - set('0123456789')) == 0

solve()

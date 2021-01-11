from collections import defaultdict


def solve():
  with open('input/q16.txt', 'r') as f:
    lines = [line[:-1] for line in f.readlines()]

  print('Answer 1:', solve1(lines[:]))
  print('Answer 2:', solve2(lines[:]))


def solve1(lines):
  classes = defaultdict(list)
  i = 0
  while lines[i] != '':
    tokens = lines[i].split(':')
    name = tokens[0]
    vals = tokens[1].strip().split('or')
    for val in vals:
      vt = val.split('-')
      mn = int(vt[0])
      mx = int(vt[1])
      classes[name].append((mn, mx))
    i += 1

  i += 5
  res = 0
  while i < len(lines):
    nums = list(map(int, lines[i].split(',')))
    a, _ = get_invalids(classes, nums)
    res += a
    i += 1

  return res

def get_invalids(classes, nums):
  res = 0
  found = False
  for num in nums:
    if not can_be_assigned(classes, num):
      res += num
      found = True
  return res, found

def can_be_assigned(classes, num):
  for c in classes:
    for interval in classes[c]:
      if fits_interval(interval, num):
        return True
  return False

def fits_interval(interval, num):
  return interval[0] <= num <= interval[1]

def solve2(lines):
  classes = defaultdict(list)
  i = 0
  while lines[i] != '':
    tokens = lines[i].split(':')
    name = tokens[0]
    vals = tokens[1].strip().split('or')
    for val in vals:
      vt = val.split('-')
      mn = int(vt[0])
      mx = int(vt[1])
      classes[name].append((mn, mx))
    i += 1

  i += 2
  ticket_nums = list(map(int, lines[i].split(',')))

  i += 3
  nearby_tickets = list()
  while i < len(lines):
    nums = list(map(int, lines[i].split(',')))
    _, found = get_invalids(classes, nums)
    if not found:
      nearby_tickets.append(nums)
    i += 1

  res = search(classes, ticket_nums, nearby_tickets)

  return res


def search(classes, ticket_nums, nearby_tickets):
  candidates = [None] * len(ticket_nums)

  for i in range(len(ticket_nums)):
    r = None
    for j in range(len(nearby_tickets)):
      clss = get_classes_for_num(nearby_tickets[j][i], classes)
      if r is None:
        r = clss
      else:
        r = r.intersection(clss)
    candidates[i] = r

  mul_count = len(ticket_nums)
  checked = set()
  while mul_count > 0:
    for i in range(len(candidates)):
      if i in checked:
        continue

      if len(candidates[i]) == 1:
        elm = list(candidates[i])[0]

        for j in range(len(candidates)):
          if j in checked or j == i:
            continue
          if elm in candidates[j]:
            candidates[j].remove(elm)

        mul_count -= 1
        checked.add(i)
  res = 1
  for i in range(len(candidates)):
    elm = list(candidates[i])[0]
    if elm.startswith('departure'):
      res *= ticket_nums[i]
  return res


def get_classes_for_num(num, classes):
  result = set()
  for c in classes:
    for interval in classes[c]:
      if fits_interval(interval, num):
          result.add(c)
          break
  return result


solve()

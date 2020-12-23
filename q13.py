from collections import defaultdict


def solve():
  with open('input/in.txt', 'r') as f:
    lines = [line[:-1] for line in f.readlines()]

  print('Answer 1:', solve1(lines[:]))
  print('Answer 2:', solve2(lines[:]))


def solve1(lines):
  earliest = int(lines[0])
  times = lines[1].split(',')
  res = -1
  resid = -1
  for time in times:
    if time == 'x':
      continue
    t = int(time)
    r = earliest + (t - (earliest % t))
    if res == -1 or res > r:
      res = r
      resid = t

  return (res-earliest) * resid


def gcd(n1, n2):
  if n2 == 0:
    return n1
  return gcd(n2, n1 % n2)


def lcm(nums):
  res = nums[0]
  for i in range(1, len(nums)):
    res = (res * nums[i]) / gcd(res, nums[i])
  return res


def solve2(lines):
  times = lines[1].split(',')

  denom_map = defaultdict(list)
  for i, time in enumerate(times):
    if time == 'x':
      continue
    t = int(time)
    denom_map[i % t].append(t)

  denom_to_lcm = dict()
  for denom in denom_map:
    l = lcm(denom_map[denom])
    denom_to_lcm[l] = denom

  mnum = max(denom_to_lcm.keys())
  res = mnum - denom_to_lcm[mnum]
  while True:
    cnt = 0
    for k in denom_to_lcm:
      if (res + denom_to_lcm[k]) % k == 0:
        cnt += 1
      else:
        break
    if cnt == len(denom_to_lcm):
      break
    res += mnum
  return res


solve()

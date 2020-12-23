from collections import defaultdict


def solve():
  with open('input/in.txt', 'r') as f:
    lines = [int(line[:-1]) for line in f.readlines()]

  print('Answer 1:', solve1(lines[:]))
  print('Answer 2:', solve2(lines[:]))


k = 25
def solve1(lines):
  for i in range(k, len(lines)):
    if not fits(lines[i - k :i], lines[i]):
      return lines[i]


def fits(nums, target):
  for i in range(len(nums)):
    for j in range(i):
      if nums[i] + nums[j] == target:
        return True
  return False


def solve2(lines):
  for i in range(k, len(lines)):
    if not fits(lines[i - k :i], lines[i]):
      return find_sum(lines, lines[i])


def find_sum(arr, target):
  a = [0] * (len(arr)+1)
  current = 0
  for i in range(len(arr)):
    a[i+1] = current + arr[i]
    current = a[i + 1]

  for i in range(len(a)):
    for j in range(i):
      if a[i] - a[j] == target:
        return min(arr[j:i]) + max(arr[j:i])

solve()

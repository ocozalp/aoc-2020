from collections import defaultdict


def solve():
  with open('input/in.txt', 'r') as f:
    lines = [line[:-1] for line in f.readlines()]

  print('Answer 1:', solve1(lines[:]))
  print('Answer 2:', solve2(lines[:]))


def solve1(lines):
  rules = dict()
  i = 0
  while lines[i] != '':
    tokens = lines[i].split(':')
    rule_id = int(tokens[0])
    rule_text = tokens[1].strip()

    if rule_text[0] == '"':
      rules[rule_id] = (True, rule_text[1:-1])
    else:
      rules_tokens = rule_text.split('|')
      sub_rules = list()
      for rule in rules_tokens:
        rule_ls = list(map(int, rule.strip().split(' ')))
        sub_rules.append(rule_ls)
      rules[rule_id] = (False, sub_rules)
    i += 1
  i += 1

  res = 0
  for line in lines[i:]:
    f, l = matches(rules, 0, line)
    if f and l == len(line):
      res += 1

  return res


def matches(rules, rule_id, text):
  if len(text) == 0:
    return False, 0

  rule = rules[rule_id]
  if rule[0]:
    return text[0] == rule[1], 1

  for rule_ls in rule[1]:
    matched_count = 0
    found = True
    for r in rule_ls:
      res, cnt = matches(rules, r, text[matched_count:])
      if not res:
        found = False
        break
      matched_count += cnt
      if matched_count > len(text):
        break

    if found:
      return True, matched_count

  return False, 0


def solve2(lines):
  rules = dict()
  i = 0
  while lines[i] != '':
    tokens = lines[i].split(':')
    rule_id = int(tokens[0])
    rule_text = tokens[1].strip()

    if rule_text[0] == '"':
      rules[rule_id] = (True, rule_text[1:-1])
    else:
      rules_tokens = rule_text.split('|')
      sub_rules = list()
      for rule in rules_tokens:
        rule_ls = list(map(int, rule.strip().split(' ')))
        sub_rules.append(rule_ls)
      if rule_id == 8:
        sub_rules.append([42, 8])
      elif rule_id == 11:
        sub_rules.append([42, 11, 31])

      rules[rule_id] = (False, sub_rules)
    i += 1
  i += 1
  res = 0
  for line in lines[i:]:
    f, l = matches2(rules, 0, line)
    if f and len(line) in l:
      res += 1
  return res


def matches2(rules, rule_id, text):
  if len(text) == 0:
    return False, {}

  rule = rules[rule_id]
  if rule[0]:
    return text[0] == rule[1], {1}

  res = set()
  for rule_ls in rule[1]:
    cnts = {0}
    for r in rule_ls:
      cnts2 = set()
      for matched_count in cnts:
        is_match, newcnts = matches2(rules, r, text[matched_count:])
        if is_match:
          for n in newcnts:
            if 0 < n+matched_count:
              cnts2.add(n + matched_count)
      cnts = cnts2

      if len(cnts) == 0:
        break

    res |= cnts

  return len(res)>0, set(res)

solve()

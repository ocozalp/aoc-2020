from collections import defaultdict


def solve():
  with open('input/q21.txt', 'r') as f:
    lines = [line[:-1] for line in f.readlines()]

  print('Answer 1:', solve1(lines[:]))
  print('Answer 2:', solve2(lines[:]))


def parse(lines):
  counts = defaultdict(int)
  allergen_ingredients = defaultdict(list)

  for line in lines:
    idx = line.find('(')
    tokens = line[: idx - 1].split(' ')
    allergens = list(map(lambda s: s.strip(), line[idx + len('contains') + 1 :-1].split(',')))
    for token in tokens:
      counts[token] += 1

    for allergen in allergens:
      allergen_ingredients[allergen].append(set(tokens))
  return allergen_ingredients, counts


def solve1(lines):
  allergen_ingredients, counts = parse(lines)

  all_suspects = set()
  for a in allergen_ingredients:
    food_list = allergen_ingredients[a]
    suspects = None
    for food in food_list:
      if suspects is None:
        suspects = food
      else:
        suspects &= food

    if suspects is not None:
      all_suspects |= suspects

  return sum([counts[i] for i in counts if i not in all_suspects])


def solve2(lines):
  allergen_ingredients, _ = parse(lines)

  all_suspects = set()
  result = dict()
  while len(result) < len(allergen_ingredients):
    for a in allergen_ingredients:
      if a in result:
        continue

      food_list = allergen_ingredients[a]
      suspects = None
      for food in food_list:
        if suspects is None:
          suspects = food
        else:
          suspects &= food
      suspects -= all_suspects

      if len(suspects) == 1:
        suspect = list(suspects)[0]
        all_suspects.add(suspect)
        result[a] = suspect
        break
  sorted_elms = [result[a] for a in sorted(result.keys())]
  return ','.join(sorted_elms)

solve()

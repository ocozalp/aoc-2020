from collections import defaultdict


operator_evals = {
  '+': lambda a, b: a + b,
  '*': lambda a, b: a * b
}


def solve():
  with open('input/q18.txt', 'r') as f:
    lines = [line[:-1] for line in f.readlines()]

  print('Answer 1:', solve1(lines[:]))
  print('Answer 2:', solve2(lines[:]))


def solve1(lines):
  return sum([evaluate(line, defaultdict(int)) for line in lines])


def evaluate(expression, precedence_map):
  operands = list()
  operators = list()
  stack = list()
  expression = expression.replace('(', ' ( ').replace(')', ' ) ')

  tokens = [token for token in expression.split(' ') if len(token.strip()) > 0]
  for token in tokens:
    if token == '(':
      stack.append((operands, operators))
      operands = list()
      operators = list()
    elif token == ')':
      val = calc(operands, operators, precedence_map)
      operands, operators = stack.pop()
      operands.append(val)
    elif token in operator_evals:
      operators.append(token)
    else:
      operands.append(int(token))
  return calc(operands, operators, precedence_map)


def calc(operands, operators, precedence_map):
  assert len(operands) == len(operators)+1
  while operators:
    idx = find_next(operators, precedence_map)

    operator = operators.pop(idx)
    oper1 = operands.pop(idx)
    oper2 = operands.pop(idx)

    operands.insert(idx, operator_evals[operator](oper1, oper2))
  return operands.pop()


def find_next(operators, precedence_map):
  res = -1
  prec = 10000
  for i, o in enumerate(operators):
    p = precedence_map[o]
    if res == -1 or p < prec:
      prec = p
      res = i
  return res


def solve2(lines):
  return sum([evaluate(line, {'+': 0, '*': 1}) for line in lines])


solve()

from collections import defaultdict
from math import sqrt


NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

NO_FLIP = 0
HOR = 1
VER = 2


def solve():
  with open('input/in.txt', 'r') as f:
    lines = [line[:-1] for line in f.readlines()]

  print('Answer 1:', solve1(lines[:]))
  print('Answer 2:', solve2(lines[:]))


def solve1(lines):
  graph, _ = construct_tile_graph(lines)

  res, tiles = search(graph)

  return res


def construct_tile_graph(lines):
  result = dict()
  tiles = dict()
  current_id = -1
  img = list()
  for line in lines:
    if line == '':
      result[current_id] = create_node(img, current_id)
      tiles[current_id] = img
      current_id = -1
      img = list()
    elif line.startswith('Tile'):
      current_id = int(line[5:-1])
    else:
      img.append(line)

  return result, tiles


def search(graph):
  visited = set()
  tiles = [None] * len(graph)
  tile_idx = [-1] * len(graph)
  dim = int(sqrt(len(graph)))
  if search_rec(graph, dim, 0, visited, tiles, tile_idx):
    return tile_idx[0]*tile_idx[dim-1]*tile_idx[-1]*tile_idx[-dim], tiles


def search_rec(graph, dim, current_tile, visited, tiles, tile_idx):
  if current_tile == len(graph):
    return True

  for k in graph:
    if k in visited:
      continue

    visited.add(k)
    for v in graph[k]:
      candidates = [v] + get_flips(v)
      for cand in candidates:
        if fits(tiles, current_tile, cand, dim):
          tiles[current_tile] = cand
          tile_idx[current_tile] = k
          if search_rec(graph, dim, current_tile + 1, visited, tiles, tile_idx):
            return True
    visited.remove(k)
  return False


def fits(tiles, current_tile, v, dim):
  result = True
  north_tile_idx = current_tile - dim
  west_tile_idx = -1 if current_tile % dim == 0 else current_tile - 1

  if north_tile_idx >= 0:
    result = result and tiles[north_tile_idx][SOUTH] == v[NORTH]

  if result and west_tile_idx >= 0:
    result = tiles[west_tile_idx][EAST] == v[WEST]

  return result


def r(s):
  return ''.join(reversed(s))


def get_flips(v):
  return [
    (v[SOUTH], r(v[EAST]), v[NORTH], r(v[WEST]), v[4], v[5], HOR),
    (r(v[NORTH]), v[WEST], r(v[SOUTH]), v[EAST], v[4], v[5], VER)
  ]


def create_node(img, tile_id):
  north = img[0]
  north_r = r(north)
  south = img[-1]
  south_r = r(south)
  west = ''.join([row[0] for row in img])
  west_r = r(west)
  east = ''.join([row[-1] for row in img])
  east_r = r(east)

  variations = [
    (north, east, south, west, tile_id, 0, NO_FLIP),  # original
    (west_r, north, east_r, south, tile_id, 1, NO_FLIP),  # ->
    (south_r, west_r, north_r, east_r, tile_id, 2, NO_FLIP),  # -> ->
    (east, south_r, west, north_r, tile_id, 3, NO_FLIP)  # -> -> ->
  ]

  return variations


def solve2(lines):
  graph, tiles = construct_tile_graph(lines)

  _, result_tiles = search(graph)
  whole_image = construct_image(tiles, result_tiles)

  for _ in range(4):
    images = [whole_image, hor_flip(whole_image), ver_flip(whole_image)]
    for cand in images:
      res = search_for_monster(cand)
      if res != -1:
        break
    whole_image = rotate_tile(whole_image)
    if res != -1:
      break
  return res


def construct_image(tiles, result_tiles):
  final_tiles = list()
  for result_tile in result_tiles:
    tile = tiles[result_tile[4]]
    for _ in range(result_tile[5]):
      tile = rotate_tile(tile)

    if result_tile[6] == HOR:
      tile = hor_flip(tile)
    elif result_tile[6] == VER:
      tile = ver_flip(tile)

    final_tiles.append(tile)

  dim = int(sqrt(len(tiles)))

  return merge_tiles(final_tiles, dim)


def merge_tiles(final_tiles, dim):
  cropped_tiles = list()
  for i, final_tile in enumerate(final_tiles):
    cropped_tile = list()

    for row in final_tile[1:-1]:
      cropped_tile.append(row[1:-1])

    cropped_tiles.append(cropped_tile)

  image = list()
  for i in range(dim):
    row_count = len(cropped_tiles[i * dim])
    for j in range(row_count):
      r = ''
      for k in range(dim):
        r += cropped_tiles[i * dim + k][j]
      image.append(r)

  return image


def rotate_tile(tile):
  res_img = [None] * len(tile)
  for i in range(len(tile)):
    res_img[i] = [None] * len(tile)

  for i in range(len(tile)):
    for j in range(len(tile)):
      res_img[i][j] = tile[len(tile) - j - 1][i]

  result = list()
  for row in res_img:
    result.append(''.join(row))
  return result


def hor_flip(tile):
  return list(reversed(tile))


def ver_flip(tile):
  result = list()
  for row in tile:
    result.append(r(row))
  return result


def search_for_monster(img):
  MONSTER_LEN = 20
  diffs = [
    (0, 0), (1, 1), (1, 4), (0, 5), (0, 6), (1, 7), (1, 10), (0, 11), (0, 12), (1, 13), (1, 16), (0, 17),
    (-1, 18), (0, 18), (0, 19)
  ]
  elms = set()
  for i, row in enumerate(img):
    if i == 0 or i == len(img) - 1:
      continue

    for j in range(len(row)):
      if j + MONSTER_LEN-1 >= len(row):
        break

      found = True
      for diff in diffs:
        r, c = diff
        if img[i + r][j + c] != '#':
          found = False
          break

      if found:
        for diff in diffs:
          r, c = diff
          elms.add((i+r, j+c))

  if len(elms) == 0:
    return - 1

  total_count = sum([len([c for c in row if c == '#']) for row in img])
  return total_count - len(elms)

solve()
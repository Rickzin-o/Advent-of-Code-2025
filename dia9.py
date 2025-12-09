# === IMPORTAÇÃO DO INPUT ===
arquivo = "inputs/dia9.txt"
given_input = ""
with open(arquivo, encoding="UTF-8") as f:
    given_input = f.read()

from itertools import combinations
import time

start_time = time.perf_counter()

# === DESAFIO 1 ===
tiles = given_input.split("\n")
tile_positions = [tuple(l.split(",")) for l in tiles]
tile_positions = list(map(lambda t: (int(t[0]), int(t[1])), tile_positions))

possible_corners = list(combinations(tile_positions, 2))
possible_corners.sort(key=lambda t: (abs(t[0][0] - t[1][0]) + 1) * (abs(t[0][1] - t[1][1]) + 1), reverse=True)
t = possible_corners[0]
area = (abs(t[0][0] - t[1][0]) + 1) * (abs(t[0][1] - t[1][1]) + 1)

end_time = time.perf_counter()
elapsed_time_seconds = end_time - start_time
elapsed_time_milliseconds = elapsed_time_seconds * 1000

print(f"Parte 1 (Executado em {elapsed_time_milliseconds:.3f}ms):", area)


# === DESAFIO 2 ===
start_time = time.perf_counter()

# Cria um perímetro baseado em pontos sequenciais
def create_polygon(positions: list):
    perimeter = set()
    total_tiles = len(positions)
    for i, tile in enumerate(positions):
        next_tile = positions[(i+1) % total_tiles]
        if tile[0] == next_tile[0]:
            for i in range(min(tile[1],next_tile[1]), max(tile[1],next_tile[1])+1):
                perimeter.add((tile[0], i))
        if tile[1] == next_tile[1]:
            for i in range(min(tile[0],next_tile[0]), max(tile[0],next_tile[0])+1):
                perimeter.add((i, tile[1]))
    return list(perimeter)

points = create_polygon(tile_positions)
print(points)


# Confere se um ponto está entre grupos de pontos
# ERRADO: Acaba conferindo pontos aleatórios
def is_between_x_axis(point, tiles, y: int):
    match_x = list(filter(lambda t: t[1]==y, tiles))
    comb = list(combinations(match_x, 2))
    for c in comb:
        c1, c2 = c
        print(point, c)
        if not (c1[1] <= point[1] <= c2[1]) and not(c2[1] <= point[1] <= c1[1]):
            return False
    return True


def is_between_y_axis(point, tiles, x: int):
    match_y = list(filter(lambda t: t[1]==x, tiles))
    comb = list(combinations(match_y, 2))
    for c in comb:
        c1, c2 = c
        print(point, c)
        if not (c1[0] <= point[0] <= c2[0]) and not(c2[0] <= point[0] <= c1[0]):
            return False
    return True

# Loop para pegar o primeiro retângulo com todos os pontos dentro do poligono maior
for p in possible_corners:
    p1, p2 = p
    count = 0
    op_corner1 = (p1[0], p2[1])
    op_corner2 = (p2[0], p1[1])
    rect = create_polygon([p1, op_corner1, p2, op_corner2])

    rect_inside = True
    print("rect", rect)
    for i in list(filter(lambda t: t[1]==p1[1], rect)):
        if not is_between_x_axis(i, points, p1[1]):
            rect_inside = False
            break
    for i in list(filter(lambda t: t[1]==p2[1], rect)):
        if not is_between_x_axis(i, points, p2[1]):
            rect_inside = False
            break
    for i in list(filter(lambda t: t[0]==p1[0], rect)):
        if not is_between_y_axis(i, points, p1[0]):
            rect_inside = False
            break
    for i in list(filter(lambda t: t[0]==p2[0], rect)):
        if not is_between_y_axis(i, points, p2[0]):
            rect_inside = False
            break

    if rect_inside:
        break

##    break
            
    

end_time = time.perf_counter()
elapsed_time_seconds = end_time - start_time
elapsed_time_milliseconds = elapsed_time_seconds * 1000

print(f"Parte 2 (Executado em {elapsed_time_milliseconds:.3f}ms): ")

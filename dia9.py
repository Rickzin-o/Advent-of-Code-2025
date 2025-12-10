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
from shapely.geometry import Polygon

polygon = Polygon(tile_positions) 

# Loop para pegar o primeiro retângulo com todos os pontos dentro do poligono maior

for p in possible_corners:
    p1, p2 = p
    count = 0
    op_corner1 = (p1[0], p2[1])
    op_corner2 = (p2[0], p1[1])
    rect = Polygon([p1, op_corner1, p2, op_corner2])

    if polygon.contains(rect):
        break

area = (abs(p[0][0] - p[1][0]) + 1) * (abs(p[0][1] - p[1][1]) + 1)

end_time = time.perf_counter()
elapsed_time_seconds = end_time - start_time
elapsed_time_milliseconds = elapsed_time_seconds * 1000

print(f"Parte 2 (Executado em {elapsed_time_milliseconds:.3f}ms): ", area)

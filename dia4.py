# === IMPORTAÇÃO DO INPUT ===
arquivo = "inputs/dia4.txt"
given_input = ""
with open(arquivo, encoding="UTF-8") as f:
    given_input = f.read()

import time
start_time = time.perf_counter()


# === DESAFIO 1 ===
map_lines = given_input.split("\n")

# Pega o número total de grids do mapa
total_x = len(map_lines[0])
total_y = len(map_lines)
total_points = total_x * total_y

def get_position_by_index(index, x_total, y_total):
    return (index % x_total, index // y_total)

# Pega os vetores das 8 direções adjacentes
directions = [[i%3-1, i//3-1] for i in range(9)]
directions.remove([0, 0])

can_access = 0
map_copy = map_lines[:]
for i in range(total_points):
    x, y = get_position_by_index(i, total_x, total_y)
    if map_lines[y][x] == ".":
        continue

    adjacents = 0
    possible_directions = set()
    for direction in directions:
        # Pega todas as direções acessíveis a partir do rolo de papel
        # Isso garante que não haverá erros com vetores para fora da margem
        vec_x, vec_y = direction[0], direction[1]
        vec_x = max(0, min(total_x - 1, x+vec_x))
        vec_y = max(0, min(total_y - 1, y+vec_y))
        if (vec_x, vec_y) == (x, y):
            continue
        possible_directions.add((vec_x, vec_y))

    for direction in possible_directions:
        # Verifica a existência de rolos nas posições possíveis
        dir_x, dir_y = direction[0], direction[1]
        adjacents += map_lines[dir_y][dir_x] == "@"

    if adjacents < 4:
        can_access += 1
        map_copy[y] = map_copy[y][:x] + "." + map_copy[y][x+1:]

end_time = time.perf_counter()
elapsed_time_seconds = end_time - start_time
elapsed_time_milliseconds = elapsed_time_seconds * 1000

print(f"Parte 1 (Executado em {elapsed_time_milliseconds:.3f}ms):", can_access)


# === DESAFIO 2 ===
start_time = time.perf_counter()

true_map_copy = map_copy[:]
removed_paper = can_access
while True:
    can_acces = 0
    map_copy = true_map_copy[:]
    for i in range(total_points):
        x, y = get_position_by_index(i, total_x, total_y)
        if map_copy[y][x] == ".":
            continue

        adjacents = 0
        possible_directions = set()
        for direction in directions:
            # Pega todas as direções acessíveis a partir do rolo de papel
            # Isso garante que não haverá erros com vetores para fora da margem
            vec_x, vec_y = direction[0], direction[1]
            vec_x = max(0, min(total_x - 1, x+vec_x))
            vec_y = max(0, min(total_y - 1, y+vec_y))
            if (vec_x, vec_y) == (x, y):
                continue
            possible_directions.add((vec_x, vec_y))

        for direction in possible_directions:
            # Verifica a existência de rolos nas posições possíveis
            dir_x, dir_y = direction[0], direction[1]
            adjacents += map_copy[dir_y][dir_x] == "@"

        if adjacents < 4:
            can_access += 1
            true_map_copy[y] = true_map_copy[y][:x] + "." + true_map_copy[y][x+1:]

        a = true_map_copy[:]
        b = map_copy[:]
        
    if "\n".join(a) == "\n".join(b):
            break

end_time = time.perf_counter()
elapsed_time_seconds = end_time - start_time
elapsed_time_milliseconds = elapsed_time_seconds * 1000

print(f"Parte 2 (Executado em {elapsed_time_milliseconds:.3f}ms):", can_access)

# === IMPORTAÇÃO DO INPUT ===
arquivo = "dia7.txt"
given_input = ""
with open(arquivo, encoding="UTF-8") as f:
    given_input = f.read()

import time
start_time = time.perf_counter()


# === DESAFIO 1 ===
map_lines = [l for l in given_input.split("\n")]

start = map_lines[0].find("S")
beams_positions = []
beams_there = []
splits = 0

def find_next_splitter(start_pos: tuple):
    global splits
    global beams_positions
    x, y = start_pos
    if (x, y) in beams_positions:
        return
    
    beams_positions.append((x, y))

    if x < 0 or x >= len(map_lines[0]) or y >= len(map_lines):
        return
    
    while True:
        y += 1
        if (x,y) in beams_positions: return
        beams_positions.append((x,y))

        # Se o próximo y estiver fora da margem, acaba com a função
        if y == len(map_lines):
            beams_there.append((x, y))
            return
        
        if map_lines[y][x] == "^":
            splits += 1
            break

    find_next_splitter((x-1, y))
    find_next_splitter((x+1, y))

find_next_splitter((start, 0))

end_time = time.perf_counter()
elapsed_time_seconds = end_time - start_time
elapsed_time_milliseconds = elapsed_time_seconds * 1000

print(f"Parte 1 (Executado em {elapsed_time_milliseconds:.3f}ms):", splits)

# === DESAFIO 2 ===
start_time = time.perf_counter()

control_line = [0 for i in range(len(map_lines[0]))]

for i, line in enumerate(map_lines):
    if i % 2 == 1: continue
    for j, v in enumerate(line):
        if v == "S": control_line[j] = 1
        if v == "^":
            control_line[j-1] += control_line[j]
            control_line[j+1] += control_line[j]
            control_line[j] = 0

end_time = time.perf_counter()
elapsed_time_seconds = end_time - start_time
elapsed_time_milliseconds = elapsed_time_seconds * 1000

print(f"Parte 2 (Executado em {elapsed_time_milliseconds:.3f}ms):", sum(control_line))

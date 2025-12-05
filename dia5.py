# === IMPORTAÇÃO DO INPUT ===
arquivo = "inputs/dia5.txt"
given_input = ""
with open(arquivo, encoding="UTF-8") as f:
    given_input = f.read()

import time
start_time = time.perf_counter()


# === DESAFIO 1 ===
id_ranges, ingredients = [x.split("\n") for x in given_input.split("\n\n")]
ingredients = list(map(lambda t: int(t), ingredients))
ordered_ranges = []
for id_range in id_ranges:
    start, end = id_range.split("-")
    ordered_ranges.append([int(start), int(end)])

ordered_ranges.sort(key=lambda t: t[0])

fresh = 0
for ingredient in ingredients:
    for r in ordered_ranges:
        if r[0] <= ingredient <= r[1]:
            fresh += 1
            break
        

end_time = time.perf_counter()
elapsed_time_seconds = end_time - start_time
elapsed_time_milliseconds = elapsed_time_seconds * 1000

print(f"Parte 1 (Executado em {elapsed_time_milliseconds:.3f}ms):", fresh)

# === DESAFIO 2 ===
start_time = time.perf_counter()

conjuntos = []
for start, end in ordered_ranges:
    if not conjuntos or conjuntos[-1][1] < start - 1:
        conjuntos.append([start, end])
    else:
        conjuntos[-1][1] = max(conjuntos[-1][1], end)

fresh_ids = sum([end - start + 1 for start, end in conjuntos])

end_time = time.perf_counter()
elapsed_time_seconds = end_time - start_time
elapsed_time_milliseconds = elapsed_time_seconds * 1000

print(f"Parte 2 (Executado em {elapsed_time_milliseconds:.3f}ms):", fresh_ids)

# === IMPORTAÇÃO DO INPUT ===
arquivo = "inputs/dia12.txt"
given_input = ""
with open(arquivo, encoding="UTF-8") as f:
    given_input = f.read()

import time

start_time = time.perf_counter()

# === DESAFIO 1 ===
info = given_input.split("\n\n")
brute_area = [x for x in info[-1].split("\n")]
areas_info = []
presents = {x.split(":\n")[0]: x.split(":\n")[-1].split("\n") for x in info[:-1]}

# Trata as informações de área e cria uma lista de dicionários
for area in brute_area:
    a, indexes = area.split(": ")
    areas_info.append({a: [int(x) for x in indexes.split()]})

def get_total_area(multiplication):
    w, h = list(map(int, multiplication.split("x")))
    return w * h

count = 0
for area in areas_info:
    key, presents = [*area.items()][0]
    w, h = list(map(int, key.split("x")))
    numeric_area = get_total_area(key)
    
    count += numeric_area > sum(presents)*7

# Isso... de alguma forma funcionou.

end_time = time.perf_counter()
elapsed_time_seconds = end_time - start_time
elapsed_time_milliseconds = elapsed_time_seconds * 1000

print(f"Parte 1 (Executado em {elapsed_time_milliseconds:.3f}ms):", count)
print("FIM.")

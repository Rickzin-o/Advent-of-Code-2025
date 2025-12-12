# === IMPORTAÇÃO DO INPUT ===
arquivo = "inputs/dia11.txt"
given_input = ""
with open(arquivo, encoding="UTF-8") as f:
    given_input = f.read()

import time

start_time = time.perf_counter()

# === DESAFIO 1 ===
connections = given_input.split("\n")
devices = [x.split(":")[0] for x in connections]
outputs = [set(x.split()[1:]) for x in connections]
graph = {devices[i]: outputs[i] for i in range(len(devices))}

count = 0
def find_paths(nodes, start, path=[]):
    # Aplicação de busca em profundidade de forma recursiva
    global count
    if start == "out":
        count += 1
        return

    for node in nodes[start]:
        if node not in path:
            path.append(node)
            find_paths(nodes, node, path)
        path.remove(node)
        

find_paths(graph, 'you')

end_time = time.perf_counter()
elapsed_time_seconds = end_time - start_time
elapsed_time_milliseconds = elapsed_time_seconds * 1000

print(f"Parte 1 (Executado em {elapsed_time_milliseconds:.3f}ms):", count)

# === DESAFIO 2 ===
start_time = time.perf_counter()
graph['out'] = {}

# Adiciona caching e fim específico na função de busca
def find_specific_paths(nodes, start, end, cache={}):
    count = 0
    if start == end:
        return 1

    if start in cache:
        return cache[start]
    
    for node in nodes[start]:
        count += find_specific_paths(nodes, node, end, cache)
    cache[start] = count

    return count

# Como sempre fft vem primeiro que dac, e out vem depois de dac...
# ...multiplicamos os caminhos possíveis de svr -> fft, fft -> dac, dac -> out
fsp = find_specific_paths
paths = fsp(graph, 'svr', 'fft', {}) * fsp(graph, 'fft', 'dac', {}) * fsp(graph, 'dac', 'out', {})

end_time = time.perf_counter()
elapsed_time_seconds = end_time - start_time
elapsed_time_milliseconds = elapsed_time_seconds * 1000

print(f"Parte 2 (Executado em {elapsed_time_milliseconds:.3f}ms): ", paths)

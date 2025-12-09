# === IMPORTAÇÃO DO INPUT ===
arquivo = "inputs/dia8.txt"
given_input = ""
with open(arquivo, encoding="UTF-8") as f:
    given_input = f.read()

from itertools import combinations
import time

start_time = time.perf_counter()
total_connections = 1000 # Variável arbitrária para o problema

# === DESAFIO 1 ===
boxes = given_input.split("\n")
possible_connections = list(combinations(boxes, 2))

def get_distance(points: tuple):
    p1, p2 = points
    x1, y1, z1 = [int(p) for p in p1.split(",")]
    x2, y2, z2 = [int(p) for p in p2.split(",")]
    distance = (x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2
    return distance

possible_connections.sort(key=get_distance)
connections_to_do = possible_connections[:total_connections]

unique_boxes = set()
for c in connections_to_do:
    unique_boxes.add(c[0])
    unique_boxes.add(c[1])

n = len(unique_boxes)
parents = list(range(n))
rank = [0] * n
unique_boxes = list(unique_boxes)
parentesco = {}

# Funções para o algoritimo de Disjoint Set
def find_parent(index):
    global parents
    if parents[index] == index:
        return index
    parents[index] = find_parent(parents[index])
    return parents[index]

def union(i, j):
    global rank
    global parents
    global n
    
    root_i = find_parent(i)
    root_j = find_parent(j)

    if root_i != root_j:
        if rank[root_i] < rank[root_j]:
            parents[root_i] = root_j
        elif rank[root_i] > rank[root_j]:
            parents[root_j] = root_i
        else:
            parents[root_j] = root_i
            rank[root_i] += 1
        n -= 1

# Faz as uniões necessárias
for c in connections_to_do:
    c1 = unique_boxes.index(c[0])
    c2 = unique_boxes.index(c[1])
    union(c1, c2)

# Confere o número das conexões
connection_parents = [find_parent(unique_boxes.index(p)) for p in unique_boxes]
number_of_connections = set([connection_parents.count(i) for i in connection_parents])
con = list(number_of_connections)

product = con[-1] * con[-2] * con[-3]

end_time = time.perf_counter()
elapsed_time_seconds = end_time - start_time
elapsed_time_milliseconds = elapsed_time_seconds * 1000

print(f"Parte 1 (Executado em {elapsed_time_milliseconds:.3f}ms):", product)


# === DESAFIO 2 ===
start_time = time.perf_counter()

n = len(boxes)
parents = list(range(n))
rank = [0] * n

def get_x(point: str):
    x, y, z = [int(i) for i in point.split(",")]
    return x

for c in possible_connections:
    c1 = boxes.index(c[0])
    c2 = boxes.index(c[1])
    union(c1, c2)

    if n == 1:
        break

extension = get_x(c[0]) * get_x(c[1])

end_time = time.perf_counter()
elapsed_time_seconds = end_time - start_time
elapsed_time_milliseconds = elapsed_time_seconds * 1000

print(f"Parte 2 (Executado em {elapsed_time_milliseconds:.3f}ms): ", extension)

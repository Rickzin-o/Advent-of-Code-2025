# === IMPORTAÇÃO DO INPUT ===
arquivo = "inputs/dia10.txt"
given_input = ""
with open(arquivo, encoding="UTF-8") as f:
    given_input = f.read()

import time
from z3 import *
from itertools import combinations

start_time = time.perf_counter()

# === DESAFIO 1 ===
machines = given_input.split("\n")
diagrams = []
buttons = []
joltages = []

# Faz os devidos tratamentos dos dados, separando nas listas
for j, m in enumerate(machines):
    info = m.split()
    info_to_joltage = m.split(" ")[-1][1:-1].split(",")

    # Aplica os diagramas em número binário e converte para decimal
    diagram_bits = list(map(lambda t: '1' if t == "#" else '0', list(info[0])[1:-1]))
    diagrams.append(int("".join(diagram_bits), 2))

    # Separa as joltagens
    joltages.append(list(map(int, filter(lambda t: t.isnumeric(), list(info_to_joltage)))))

    # Converte cada botão em um decimal e junta os grupos
    temp_list = []
    for i in info[1:-1]:
        b = list(filter(lambda t: t.isnumeric(), list(i)))
        pressed = ['0'] * len(diagram_bits)
        for n in b: pressed[int(n)] = '1'
        temp_list.append(int("".join(pressed[:]), 2))
    buttons.append(temp_list[:])

##menores = [15] * len(diagrams)
menores = [len(b) for b in buttons]


def press_buttons_by_combinations(diagram, buttons_list, n):
    possible_groups = list(combinations(buttons_list, n))
    for g in possible_groups:
        count = 0
        for b in g:
            count = count ^ b
        if count == diagram:
            return True
    return False

solved = [False for d in diagrams]
for i, diagram in enumerate(diagrams):
    n = 1
    while not solved[i]:
        solved[i] = press_buttons_by_combinations(diagram, buttons[i], n)
        n += 1
        if n == len(buttons[i]) + 1:
            break
    menores[i] = n - 1

end_time = time.perf_counter()
elapsed_time_seconds = end_time - start_time
elapsed_time_milliseconds = elapsed_time_seconds * 1000

print(f"Parte 1 (Executado em {elapsed_time_milliseconds:.3f}ms):", sum(menores))


# === DESAFIO 2 ===
start_time = time.perf_counter()

buttons = []
for j, m in enumerate(machines):
    info = m.split()
    diagram_bits = list(map(lambda t: '1' if t == "#" else '0', list(info[0])[1:-1]))
    temp_list = []
    for i in info[1:-1]:
        b = list(filter(lambda t: t.isnumeric(), list(i)))
        pressed = ['0'] * len(diagram_bits)
        for n in b: pressed[int(n)] = '1'
        temp_list.append(list(map(int, pressed[:])))
    buttons.append(temp_list[:])

# Usa álgebra linear para encontrar coeficientes que formar o vetor joltage
count = 0
counts = [0] * len(joltages)
for i, joltage in enumerate(joltages):
    variables = [Int(f'k_{i}') for i in range(len(buttons[i]))]
    soma = [0] * len(joltage)
    base = buttons[i]

    s = Optimize()
    
    for j, b in enumerate(buttons[i]):
        s.add(variables[j] >= 0)
        for k in range(len(joltage)):
            soma[k] += variables[j] * b[k]

    for j, eq in enumerate(soma):
        simple_eq = simplify(eq)
        s.add(simple_eq == joltage[j])

    a = 0
    for var in variables:
        a += var
    s.minimize(simplify(a))
    
    if s.check() == sat:
        count = 0
        m = s.model()
        block = []
        for var in variables:
            count += (m[var])

        count = simplify(count)
        counts[i] = int(str(count))
        
    


end_time = time.perf_counter()
elapsed_time_seconds = end_time - start_time
elapsed_time_milliseconds = elapsed_time_seconds * 1000

print(f"Parte 2 (Executado em {elapsed_time_milliseconds:.3f}ms): ", sum(counts))

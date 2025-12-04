# === IMPORTAÇÃO DO INPUT ===
arquivo = "inputs/dia3.txt"
given_input = ""
with open(arquivo, encoding="UTF-8") as f:
    given_input = f.read()

from itertools import combinations
import time

start_time = time.perf_counter()

# === DESAFIO 1 ===
combinacoes = []
banks = given_input.split("\n")
maiores = []

maior_atual = 0
for bank in banks:
    bank = [x for x in bank]
    combinacoes = list(combinations(bank, 2))
    
    for comb in combinacoes:
        numero = int(comb[0]+comb[1])
        maior_atual = max(numero, maior_atual)
    
    maiores.append(maior_atual)
    maior_atual = 0
    combinacoes = []
    
end_time = time.perf_counter()
elapsed_time_seconds = end_time - start_time
elapsed_time_milliseconds = elapsed_time_seconds * 1000

print(f"Parte 1 (Executado em {elapsed_time_milliseconds:.3f}ms):", sum(maiores))


# === DESAFIO 2 ===
start_time = time.perf_counter()

def maximo_subint(string, size):
    if size == 1:
        return max(string)
    n = len(string)
    ind, maximo = max(enumerate(string[0:n-size+1]), key=lambda t: t[1])
    return maximo + maximo_subint(string[ind+1:], size-1)

maior_atual = 0
for bank in banks:
    maior_atual += int(maximo_subint(bank, 12))
    

end_time = time.perf_counter()
elapsed_time_seconds = end_time - start_time
elapsed_time_milliseconds = elapsed_time_seconds * 1000

print(f"Parte 2 (Executado em {elapsed_time_milliseconds:.3f}ms): ", maior_atual)

# === IMPORTAÇÃO DO INPUT ===
arquivo = "dia6.txt"
given_input = ""
with open(arquivo, encoding="UTF-8") as f:
    given_input = f.read()

import time
start_time = time.perf_counter()


# === DESAFIO 1 ===
information = [l.split() for l in given_input.split("\n")]

total = 0
for i, op in enumerate(information[-1]):
    if op == "+":
        total += sum([int(information[j][i]) for j in range(len(information)-1)])
    if op == "*":
        mult = 1
        for j in range(len(information)-1):
            mult *= int(information[j][i])
        total += mult
        

end_time = time.perf_counter()
elapsed_time_seconds = end_time - start_time
elapsed_time_milliseconds = elapsed_time_seconds * 1000

print(f"Parte 1 (Executado em {elapsed_time_milliseconds:.3f}ms):", total)

# === DESAFIO 2 ===
start_time = time.perf_counter()

# Faremos a leitura da direita para a esquerda
inverted_input = [l[::-1] for l in given_input.split("\n")]

length_input = len(inverted_input[0])
last_op = save_op = 0
blank_space = False
matriz_numeros = [[] for l in inverted_input]
matriz_numeros.pop()
save_matriz = [[] for l in inverted_input]
save_matriz.pop()

total = 0
for i, v in enumerate(inverted_input[-1]):
    # Pega index e valor de cada CARACTERE da última linha.
    # Talvez esse caractere seja espaço, talvez seja operador
    if blank_space:
        blank_space = False
        continue

    # Adiciona os números na matriz
    for j, l in enumerate(matriz_numeros):
        char = inverted_input[j][i]
        char = '0' if char == " " else char
        l.append(int(char))
    
    last_op = i if v != " " else save_op
    if last_op != save_op:
        # Faz os devidos cálculos ao chegar no operador
        group_total = 0 if v == "+" else 1
        for j in range(len(matriz_numeros[0])):
            # Monta a "ideia" da leitura do número colocando em uma linha
            # Os zeros serão eliminados depois, pois representam apenas
            # espaços, e percebe-se que não há zeros no input
            matriz_linha = []
            for k, l in enumerate(matriz_numeros):
                if l[j] != 0: matriz_linha.append(str(l[j]))
            numero = int("".join(matriz_linha))
            group_total = group_total + numero if v == "+" else group_total * numero

        # Reseta informações para próximo grupo de cálculo
        blank_space = True
        save_op = last_op
        matriz_numeros = [l[:] for l in save_matriz]
        total += group_total


end_time = time.perf_counter()
elapsed_time_seconds = end_time - start_time
elapsed_time_milliseconds = elapsed_time_seconds * 1000

print(f"Parte 2 (Executado em {elapsed_time_milliseconds:.3f}ms):", total)

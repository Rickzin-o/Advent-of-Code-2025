# === IMPORTAÇÃO DO INPUT ===
arquivo = "inputs/dia2.txt"
given_input = ""
with open(arquivo, encoding="UTF-8") as f:
    given_input = f.read()


# === DESAFIO 1 ===
ranges = given_input.split(",")
numbers = [[x.split("-")[0], x.split("-")[1]] for x in ranges]
counter = 0
for r in numbers:
    if len(r[0]) % 2 == 1 and len(r[1]) % 2 == 1:
        continue
    for i in range(int(r[0]), int(r[1])+1):
        tamanho_numero = len(str(i))
        if tamanho_numero % 2 == 1:
            continue
        tamanho_metade = tamanho_numero // 2
        if str(i)[:tamanho_metade] == str(i)[tamanho_metade:]:
            counter += i

print("PARTE 1:", counter)


# === DESAFIO 2 ===
def divisores_de(n):
    sqrt = int(n**(1/2))
    divisores = set()
    for i in range(1, sqrt+1):
        if n % i == 0:
            divisores.add(i)
            divisores.add(n//i)
    lista_divisores = list(divisores)
    lista_divisores.sort()
    return lista_divisores[:-1]


def dividir_string(string_original, n):
    tamanho_total = len(string_original)
    tamanho_pedaco = tamanho_total // n
    pedacos = []
    inicio = 0
    for i in range(n):
        fim = inicio + tamanho_pedaco
        pedacos.append(string_original[inicio:fim])
        inicio = fim
    return pedacos

counter = 0
for r in numbers:
    for i in range(int(r[0]), int(r[1])+1):
        tamanho_numero = len(str(i))
        for div in divisores_de(tamanho_numero):
            contagem = 0
            tudo_igual = True
            pedacos_numero = dividir_string(str(i), tamanho_numero//div)
            for j, pedaco in enumerate(pedacos_numero):
                if pedacos_numero[j] != pedacos_numero[j-1]:
                    tudo_igual = False
            if tudo_igual:
                counter += i
                break

print("PARTE 2:", counter)

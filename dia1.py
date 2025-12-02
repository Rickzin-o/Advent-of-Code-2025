# === IMPORTAÇÃO DO INPUT ===
arquivo = "inputs/dia1.txt"
given_input = ""
with open(arquivo, encoding="UTF-8") as f:
    given_input = f.read()


# === DESAFIO 1 ===
apontando_para = 50
lista_rotacoes = given_input.split("\n")
rotacoes = []

for rotacao in lista_rotacoes:
    if rotacao[0] == "R":
        rotacoes.append(int(rotacao[1:]))
    else:
        rotacoes.append(-int(rotacao[1:]))

aponta_zero = 0
for rotacao in rotacoes:
    apontando_para += rotacao
    apontando_para %= 100
    aponta_zero += 1 if apontando_para == 0 else 0

print("DESAFIO 1:", aponta_zero)


# === DESAFIO 2 ===
apontando_para = 50
passou_no_zero = 0

for i, rotacao in enumerate(rotacoes):
    anterior = apontando_para
    apontando_para += rotacao
    divisao_inteira, resto = apontando_para // 100, apontando_para % 100
    # Adiciona o número de vezes que passou no 0, vulgo a divisão euclidiana de 100
    passou_no_zero += abs(divisao_inteira)
    # Como um número negativo acaba tendo um valor absoluto na divisão em 1
    # casa acima se não tiver resto 0, retiramos esses casos (ex: -305//100 = -4)
    passou_no_zero -= (anterior == 0 and (divisao_inteira) < 0)
    # Mas caso seja resto 0, precisamos manter, então adicionamos +1 nestes casos
    passou_no_zero += (resto == 0 and rotacao < 0)
    apontando_para %= 100
                           

print("DESAFIO 2:", passou_no_zero)

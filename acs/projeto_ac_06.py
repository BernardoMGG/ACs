# Exercícios em Aula p/ o Beecrowd 19/03

# Jogando Cartas Fora (1110):
def jogando_cartas_fora():
    while True:
        n = int(input())
        if n == 0:
            break

        lista = list(range(n, 0, -1))
        descartados = []
        while len(lista) > 1:
            descartados.append(lista.pop())
            lista.insert(0, lista.pop())

        descartados = [str(num) for num in descartados]
        print("Discarded cards: ", descartados)
        print("Remaining card:", lista[0])

# Diamantes e Areia (1069):
def diamantes_e_areias():
    n = int(input())

    for _ in range(n):
        entrada = input()
        extracao = []
        diamantes = 0
        for char in entrada:
            if char == ".":
                continue
            if char == "<":
                extracao.append(char)
            else:
                if len(extracao) >= 1 and extracao[-1] == "<":
                    extracao.pop()
                    diamantes += 1

    print(diamantes)

# Calculo Simples:
def calculo_simples():
    dados1 = input()
    dados2 = input()

    dados1 =dados1.split(" ")
    dados2 = dados2.split(" ")

    preco = int(dados1[1]) * float(dados1[2]) + int(dados2[1]) * float(dados2[2])
    print(f"Valor a Pagar: R$ {preco:.2f}")

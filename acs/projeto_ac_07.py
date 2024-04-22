# Aumento de Salário (1048):
def aumento_salarial():
    salario = float(input(""))
    if salario >= 0 and salario <= 400:
        reajuste = salario * 0.15
        salario = salario + reajuste
        print(f"Novo salario: {salario:.2f}")
        print(f"Reajuste ganho: {reajuste:.2f}")
        print("Em percentual: 15 %")
    elif salario >= 400.01 and salario <= 800:
        reajuste = salario * 0.12
        salario = salario + reajuste
        print(f"Novo salario: {salario:.2f}")
        print(f"Reajuste ganho: {reajuste:.2f}")
        print("Em percentual: 12 %")
    elif salario >= 800.01 and salario <= 1200:
        reajuste = salario * 0.1
        salario = salario + reajuste
        print(f"Novo salario: {salario:.2f}")
        print(f"Reajuste ganho: {reajuste:.2f}")
        print("Em percentual: 10 %")
    elif salario >= 1200.01 and salario <= 2000:
        reajuste = salario * 0.07
        salario = salario + reajuste
        print(f"Novo salario: {salario:.2f}")
        print(f"Reajuste ganho: {reajuste:.2f}")
        print("Em percentual: 7 %")
    elif salario > 2000:
        reajuste = salario * 0.04
        salario = salario + reajuste
        print(f"Novo salario: {salario:.2f}")
        print(f"Reajuste ganho: {reajuste:.2f}")
        print("Em percentual: 4 %")

"aumento_salarial()"

# Pares entre Cinco Números (1065):
def pares_de_cinco():
    qtd = 0
    for _ in range(5):
        num = int(input())
        if num % 2 == 0:
            qtd += 1
    print(qtd, "valores pares")

"pares_de_cinco()"
    
# Múltiplo de 13 (1132):
def multiplo():
    x = int(input(""))
    y = int(input(""))
    soma = 0
    if x > y:
        ma = x
        mi = y
    else:
        ma = y
        mi = x
    for i in range(mi, ma + 1):
        if i % 13 != 0:
            soma += i
    print(soma)

"multiplo()"

# Preenchimento de Vetor (1173):
def vetor():
    v = int(input(""))
    n = [0] * 10
    n[0] = v
    for i in range(1, 10):
        n[i] = n[i - 1] * 2
    for i in range(10):
        print("N[", i, "] = ", n[i], sep="")

"vetor()"

# Menor e Posição (1180):
def posicao():
    tamanho = int(input())
    valores = [int(x) for x in input().split()]

    menor, posicao = valores[0], 0

    for id, valor in enumerate(valores):
        if valor < menor:
            menor, posicao = valor, id

    print("Menor valor:", menor)
    print("Posicao:", posicao)

"posicao()"

# Coluna na Matriz (1182):
def matriz():
    coluna = int(input())
    operacao = input()

    m = []
    for _ in range(12):
        linha = [float(x) for x in input().split()]
        m.append(linha)

    elementos_area_verde = [m[i][coluna] for i in range(1, 11)]

    if operacao == 'S':
        resultado = sum(elementos_area_verde)
    elif operacao == 'M':
        resultado = sum(elementos_area_verde) / len(elementos_area_verde)

    print(f"{resultado:.1f}")

"matriz()"

# Ordenação por Tamanho (1244):
def ordenar_por_tamanho(strings):
    return sorted(strings, key=lambda x: (len(x), strings.index(x)))
N = int(input())
conjunto_strings_ordenado = []
for _ in range(N):
    strings = input().split()
    conjunto_strings_ordenado.append(ordenar_por_tamanho(strings))
for conjunto in conjunto_strings_ordenado:
    print(' '.join(conjunto))

ordenar_por_tamanho()
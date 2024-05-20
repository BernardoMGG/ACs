# Distancia (1016):
def corrida():
    km = int(input())
    tempo = km * 2
    print(f"{tempo} minutos")

'corrida()'

# Fatorial Simples (1153):
def fatorial():
    n = int(input())
    fat = 1
    for i in range(1, n + 1):
        fat *= i
    print(fat)

'fatorial()'

# Ida à feira (1281):
def feira():
    n = int(input())
    while(n > 0):
        n -= 1

        m = int(input())

        produtos = {}
        for i in range(m):
            produto = input()
            produto = produto.split()
            produtos[produto[0]] = float(produto[1]) # convertendo o produto para um par {string:float} = {nome:valor}

        p = int(input())
        total = 0.0
        for i in range(p):
            produto = input()
            produto = produto.split()
            nome_produto = str(produto[0])
            qtd_produto = int(produto[1])
            total = total + produtos[nome_produto] * qtd_produto # convertendo o produto para um par {string:int} = {nome:quantidade}
        print ("R$ %.2f" % total)

'feira()'

# Identificando o Chá (2006):
def indentificando():
    T = int(input())
    A,B,C,D,E = input().split(' ')
    A = int(A)
    B = int(B)
    C = int(C)
    D = int(D)
    E = int(E)
    numbers = [A,B,C,D,E]
    print(numbers.count(T))

'indentificando()'


# Aviões de Papel (2339):
def avioes():
    lista = input()
    lista = lista.split(" ")
    c = int(lista[0])
    p = int(lista[1])
    f = int(lista[2])
    if c * f <= p:
        print("S")
    else:
        print("N")

'avioes()'

# Tacógrafo (2388):
def tacografo():
    n = int(input())
    soma = 0
    for _ in range (n):
        t,v = map(int,input().split())
        soma = soma + (t * v)
    print(soma)

'tacografo()'

# Busca na Internet (2413):
def busca():
    pessoas = int(input())
    click = pessoas * 4
    print(f"{click}")

'busca()'

# Sequência Secreta (3048):
def secret():
    n = int(input())
    a = 0
    s = 0
    for i in range (n):
        v = int(input())
        if v != a:
            a = v
            s = s + 1
    print(s)

'secret()'
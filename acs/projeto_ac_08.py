# Figurinhas (1028):
def mdc(a, b):
    while b:
        a, b = b, a % b
    return a

def max_pilha(f1, f2):
    dc = mdc(f1, f2)
    return dc

def figurinhas():
    n = int(input())
    for _ in range(n):
        f1, f2 = map(int, input().split())
        print(max_pilha(f1, f2))

'figurinhas()'

# Dama (1087):
def min_mov_dama(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    return max(dx, dy)

def dama():
    while True:
        x1, y1, x2, y2 = map(int, input().split())
        if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0:
            break
        print(min_mov_dama(x1, y1, x2, y2))

'dama()'

# Soma dos Fatorias: (1161):
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

def soma_deles():
    while True:
        try:
            M, N = map(int, input().split())
            print(fatorial(M) + fatorial(N))
        except EOFError:
            break

'soma_deles()'

# Blobs (1170):
def calcular_dias(capacidade):
    dias = 0
    while capacidade > 1:
        capacidade /= 2
        dias += 1
    return dias

def blobs():
    N = int(input())

    for _ in range(N):
        qtd = float(input())
        print(f"{calcular_dias(qtd)} dias")

'blobs()'

# Frequência de Números (1171):
def frequencia():
    N = int(input())
    qtd = {}

    for _ in range(N):
        valor = int(input())
        if valor in qtd:
            qtd[valor] += 1
        else:
            qtd[valor] = 1

    n_ordenados = sorted(qtd.keys())

    for numeros in n_ordenados:
        print(f"{numeros} aparece {qtd[numeros]} vez(es)")

'frequencia()'

# Primo Rápido (1221):
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def primo_rapido():
    N = int(input())
    for _ in range(N):
        X = int(input())
        if is_prime(X):
            print("Prime")
        else:
            print("Not Prime")

'primo_rapido()'

# Cara ou Coroa (1329):
def contar_vitorias(resultados):
    mv = resultados.count(0)
    jv = resultados.count(1)
    return mv, jv

def cara_coroa():
    while True:
        N = int(input()) 
        if N == 0:
            break
        resultados = list(map(int, input().split()))
        maria, joao = contar_vitorias(resultados)
        print(f"Mary won {maria} times and John won {joao} times")

'cara_coroa()'

# Função (1555):
def r(a, b):
    return (3*a)**2 + b**2

def b(a, b):
    return 2*(a**2) + (5*b)**2

def c(a, b):
    return -100*a + b**3

def funcao():
    N = int(input())
    for _ in range(N):
        a, b = map(int, input().split())
        resultado_r = r(a, b)
        resultado_b = b(a, b)
        resultado_c = c(a, b)
        if resultado_r > resultado_b and resultado_r > resultado_c:
            print("Rafael ganhou")
        elif resultado_b > resultado_r and resultado_b > resultado_c:
            print("Beto ganhou")
        else:
            print("Carlos ganhou")

'funcao()'


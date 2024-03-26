# Hello World! (1000):
print("Hello World!")

# # Extremamente Básico (1001):
a = int(input())
b = int(input())
x = a + b
print("X =", x)

# Calculo Simples (1010):
def calculo_simples():
    dados1 = input()
    dados2 = input()

    dados1 =dados1.split(" ")
    dados2 = dados2.split(" ")

    preco = int(dados1[1]) * float(dados1[2]) + int(dados2[1]) * float(dados2[2])
    print(f"Valor a Pagar: R$ {preco:.2f}")

# O Maior (1013)
def maior():
    quantia = input()
    quantia = quantia.split(" ")

    x = int(quantia[0])
    y = int(quantia[1])
    z = int(quantia[2])

    xy = ((x + y + abs (x - y)) /2)
    xz = ((x + z + abs (x - z)) /2)
    yz = ((y + z +abs(y - z)) /2)

    if xy == xz:
        print(x, "eh o maior")
    if xy == yz:
        print(y, "eh o maior")
    if xz == yz:
        print(z, "eh o maior")

# Distância entre Dois Pontos (1015)
def distância_entre_2():
    x = input()
    y = input()

    x = x.split(" ")
    y = y.split(" ")

    x1= float(a[0])
    y1 = float(a[1])

    x2 = float(b[0])
    y2 = float(b[1])

    distanciaab = (((x2 - x1)**2) + ((y2 - y1)**2))**(1/2)

    print(f"{distanciaab:.4}")

def determina_tipo_triangulo(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Não é um triângulo"
    if a == b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"

def teste_identificação():
    print(determina_tipo_triangulo(3, 3, 3))  # Saída: Equilátero
    print(determina_tipo_triangulo(3, 4, 3))  # Saída: Isósceles
    print(determina_tipo_triangulo(3, 4, 5))  # Saída: Escaleno
    print(determina_tipo_triangulo(1, 1, 3))  # Saída: Não é um triângulo

def dia_semana(numero):
    dias_semana = ["Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado"]
    
    if numero >= 1 and numero <= 7:
        return dias_semana[numero - 1]
    else:
        return "Dia inválido"

def teste_dia():
    print(dia_semana(1))  # Saída: Domingo
    print(dia_semana(2))  # Saída: Segunda-feira
    print(dia_semana(7))  # Saída: Sábado
    print(dia_semana(0))  # Saída: Dia inválido 
    print(dia_semana(8))  # Saída: Dia inválido

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro"
    else:
        return a / b

def calculadora():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação desejada(+, -, * ou /): ")

    if operacao == "+":
        resultado = soma(num1, num2)
    elif operacao == "-":
        resultado = subtracao(num1, num2)
    elif operacao == "*":
        resultado = multiplicacao(num1, num2)
    elif operacao == "/":
        resultado = divisao(num1, num2)
    else:
        resultado = "Operação inválida"
    print("Resultado:", resultado)

def main():
    teste_identificação()
    teste_dia()
    calculadora()

main()
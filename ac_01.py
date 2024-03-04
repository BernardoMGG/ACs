def calcular_raizes():
    a = float(input("Informe o parâmetro a da equação: "))
    b = float(input("Informe o parâmetro b da equação: "))
    c = float(input("Informe o parâmetro c da equação: "))

    delta = b ** 2 - 4 * a * c
    x1 = (-b + delta ** 1/2) / (2 * a)
    x2 = (-b - delta ** 1/2) / (2 * a)
    print("As raízes são:", x1, "e", x2)

def bissexto(): 
    ano = int(input("Digite o ano: "))
    eh_bissexto = (ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0)
    print("O ano", ano, "é bissexto?" , eh_bissexto)

def main():
    calcular_raizes()
    bissexto()

main()
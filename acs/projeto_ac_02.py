def calcular_raizes(a, b, c):
    delta = b ** 2 - 4 * a * c
    x1 = (-b + delta ** 1/2) / (2 * a)
    x2 = (-b - delta ** 1/2) / (2 * a)
    print("As raízes são:", x1, "e", x2)

def bissexto(ano):
    eh_bissexto = (ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0)
    print("O ano", ano, "é bissexto?" , eh_bissexto)

def calcula_salario(valor_hora, num_horas):
    irpf = 0.275
    salario_bruto = valor_hora * num_horas
    imposto_renda = salario_bruto * irpf
    salario_liquido = salario_bruto - imposto_renda
    print("Seu salário liquido é:", salario_liquido)

def main():
    calcular_raizes(2, 4, 4)
    bissexto(400)
    calcula_salario(1200, 8)

main()
# Exercício AC4 05/03/2024:


def usuario():
    """
    Pede para o usuário informar o nome, e retorna uma string.
    """
    return input("Informe o seu nome: ")

def ler_notas():
    """
    Lê e retorna quatro notas do tipo float.
    """
    ap1 = float(input("Informe sua AP1: "))
    ap2 = float(input("Informe sua AP2: "))
    ac = float(input("Informe sua AC: "))
    asub = float(input("Informe sua AS: "))
    return ap1, ap2, ac, asub

def validar_notas(ap1, ap2, asub, ac):
    """
    Retorna False se pelo menos uma das notas for menor que zero ou
    maior que dez.
    """
    if ap1 > 10 or ap1 < 0:
        return False
    if ap2 > 10 or ap2 < 0:
        return False
    if ac > 10 or ac < 0:
        return False
    if asub > 10 or asub < 0:
        return False
    else:
        return True

def duas_maiores_notas(ap1, ap2, asub):
    """
    Retorna as duas maiores notas dentre as informadas.
    """
    if ap1 < asub:
        return asub, ap2
    elif ap2 < asub:
        return ap1, asub
    return ap1, ap2

def calcular_media(n1, n2, ac):
    """
    Calcula e retorna a média do usuário.
    """
    return (n1 + n2) * 0.4 + ac * 0.2

def informar_aprovacao(media):
    """
    Informa se o aluno passou ou não na disciplina.
    """
    print("Sua média foi", round(media, 2))
    if media >= 7:
        print("Parabéns, você foi aprovado!")
    else:
        print("Você foi reprovado...")

def main():
    nome = usuario()
    if nome:
        ap1, ap2, asub, ac = ler_notas()
        if validar_notas(ap1, ap2, asub, ac):
            n1, n2 = duas_maiores_notas(ap1, ap2, asub)
            media = calcular_media(n1, n2, ac)
            informar_aprovacao(media)

main()
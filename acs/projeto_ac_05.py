# Exercício AC5 12/03/2024

import random

# Gera valores aleatórios entre 2 e 8
# print(random.randint(2, 8))

def jogo():
    vida_a = 100
    att_a = random.randint(10, 20)
    def_a = random.randint(1, 5)
    print("Aventureiro: Vida: ", vida_a, "Ataque:", att_a, "Defesa: ", def_a)
    vida_m = random.randint(60, 80)
    att_m = random.randint(20, 30)
    def_m = 0
    print("Monstro: Vida: ", vida_m, "Ataque:", att_m, "Defesa: ", def_m)

    rodadas = 1

    while vida_a > 0 or vida_m > 0:
        print("Rodada: ", rodadas)
        vida_m = vida_m - random.randint(1, att_a)
        if vida_m <= 0:
            print("Monstro morreu!")
            break
        dano = random.randint(1, att_m) + def_a
        if dano > 0:
            vida_a = vida_a - dano
        if vida_a <=0:
            print("Aventureiro morreu!")
            break
        print("Vida do Aventureiro: ", vida_a)
        print("Vida do Monstro: ", vida_m)
        rodadas += 1

jogo()
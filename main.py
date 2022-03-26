import os
import math
import re

while True:
    while True:
        Ax = input("Valor X do ponto A: ")
        x = re.findall("[a-zA-Z]", Ax)
        if x:
            print('Valor invalido!')
            os.system('cls')
        else:
            ax = int(Ax)
            os.system('cls')
            break

    while True:
        Ay = input("Valor Y do ponto A: ")
        x = re.findall("[a-zA-Z]", Ay)
        if x:
            print('Valor invalido!')
            os.system('cls')
        else:
            ay = int(Ay)
            os.system('cls')
            break

    while True:
        Bx = input("Valor X do ponto B: ")
        x = re.findall("[a-zA-Z]", Bx)
        if x:
            print('Valor invalido!')
            os.system('cls')
        else:
            bx = int(Bx)
            os.system('cls')
            break

    while True:
        By = input("Valor Y do ponto B: ")
        x = re.findall("[a-zA-Z]", By)
        if x:
            print('Valor invalido!')
            os.system('cls')
        else:
            by = int(By)
            os.system('cls')
            break

    X = ax - bx
    Y = ay - by
    X = X**2
    Y = Y**2

    Distance = X + Y

    try:
        Distance = math.sqrt(Distance)
        print(f"A distancia entre ({Ax},{Bx}) e ({Bx},{By}) é ({Distance}), ou (√{Distance*Distance})")
        input("pressione qualquer tecla para outro calculo")
        os.system('cls')
    except:
        # os.system('cls')
        print(f"Falha ao tentar calcular, tente novamente")
        input("pressione qualquer tecla para um novo calculo")
        os.system('cls')

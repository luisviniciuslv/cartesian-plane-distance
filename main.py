import os
import math
while True:
    while True:
        Ax = input("Valor X do ponto A: ")
        if Ax.isnumeric() or Ax[0] == "-":
            ax = int(Ax)
            os.system('cls')
            break
        else:
            print("digite um valor válido")
    while True:
        Ay = input("Valor Y do ponto A: ")
        if Ay.isnumeric() or Ay[0] == "-":
            ay = int(Ay)
            os.system('cls')
            break
        else:
            print("digite um valor válido")

    while True:
        Bx = input("Valor X do ponto B: ")
        if Bx.isnumeric() or Bx[0] == "-":
            bx = int(Bx)
            os.system('cls')
            break
        else:
            print("digite um valor válido")

    while True:
        By = input("Valor Y do ponto B: ")
        if By.isnumeric() or By[0] == "-":
            by = int(By)
            os.system('cls')
            break
        else:
            print("digite um valor válido")

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

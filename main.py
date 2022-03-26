import os
import math
import re
from pylab import *
import matplotlib.pyplot as plt


while True:
    while True:
        Ax= input("Valor X do ponto A: ")
        cAx = Ax
        x = re.findall("[a-zA-Z]", Ax)
        if x:
            os.system('cls')
            print('Valor invalido!')
        else:
            try:
                ax = int(Ax)
                os.system('cls')
                break
            except:
                print('Valor invalido!')

    while True:
        Ay= input("Valor Y do ponto A: ")
        cAy = Ay
        x = re.findall("[a-zA-Z]", Ay)
        if x:
            print('Valor invalido!')
            os.system('cls')
        else:
            try:
                ay = int(Ay)
                os.system('cls')
                break
            except:
                print('Valor invalido!')

    while True:
        Bx = input("Valor X do ponto B: ")
        cBx = Bx
        x = re.findall("[a-zA-Z]", Bx)
        if x:
            print('Valor invalido!')
            os.system('cls')
        else:
            try:
                bx = int(Bx)
                os.system('cls')
                break
            except:
                print('Valor invalido!')

    while True:
        By= input("Valor Y do ponto B: ")
        cBy = By
        x = re.findall("[a-zA-Z]", By)
        if x:
            print('Valor invalido!')
            os.system('cls')
        else:
            try:
                by = int(By)
                os.system('cls')
                break
            except:
                print('Valor invalido!')

    X = ax - bx
    Y = ay - by
    X = X**2
    Y = Y**2
    Distance = X + Y

    try:
        Distance = math.sqrt(Distance)
        print(f"A distancia entre ({Ax},{Ay}) e ({Bx},{By}) é ({Distance}), ou (√{Distance*Distance})")
        def on_close(event):
            print('Closed Figure!')

        fig = plt.figure()
        fig.canvas.mpl_connect('close_event', on_close)
        plt.xlabel(f'A = {int(cAx), int(cAy)} B = {int(cBx), int(cBy)}')
        plt.title(f'distance = {Distance}')
        plt.plot([int(cAx), int(cAy)], [int(cBx), int(cBy)], marker='o')
        plt.show()
        os.system('cls')
        
    except:
        print(f"Falha ao tentar calcular, tente novamente")
        input("pressione qualquer tecla para um novo calculo")
        os.system('cls')

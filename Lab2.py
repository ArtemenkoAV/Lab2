import control.matlab as matlab
import matplotlib.pyplot as plt
import numpy as numpy
import math
import sys
import sympy


newChoise = True
while newChoise:
    userInput = input("Введите номер нужной обратной связи: \n"
                      "1 - Жесткая обратная связь \n"
                      "2 - Гибкая обратная связь \n"
                      "3 - Апериодическая жесткая обратаная связь\n"
                      "4 - апериодически гибкая обратная связь.\n")
    if userInput.isdigit():
        newChoise = False
        userInput = int(userInput)
        if userInput == 1:
            kos = float(input("Kos= "))
            w1 = matlab.tf([kos], [1])

        elif userInput == 2:
            kos = float(input("Kos= "))
            w1 = matlab.tf([kos, 0], [1])
        elif userInput == 3:
            kos = float(input("Kos= "))
            tos = float(input("Tos= "))
            w1 = matlab.tf([kos], [tos, 1])
        elif userInput == 4:
            kos = float(input("Kos= "))
            tos = float(input("Tos= "))
            w1 = matlab.tf([kos, 0], [tos, 1])
        else:
            print('Введите допустимое значение!')
    else:
        print("Введите допустимое значение!")
    def W1
        newChoise = True









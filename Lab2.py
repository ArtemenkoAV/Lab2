import control.matlab as matlab
import matplotlib.pyplot as pyplot
import numpy as numpy
import math
import sys
from sympy import *

# ввод исходных данных


choiseOS = True
while choiseOS:
    userInput = input("Введите номер нужной обратной связи: \n"
                      "1 - Жесткая обратная связь \n"
                      "2 - Гибкая обратная связь \n"
                      "3 - Апериодическая жесткая обратаная связь\n"
                      "4 - апериодически гибкая обратная связь.\n")
    if userInput.isdigit():
        choiseOS = False
        userInput = int(userInput)
        if userInput == 1:
            os = True
            while os:
                print("Введите исходные данные")
                kos = input("Kos = ")
                if kos.replace('.', '', 1).isdigit():   # проверка чтоб пользователь вводил только числовые значения
                    kos = float(kos)
                    wos = matlab.tf([kos], [1])

                    os = False
                else:
                    print("Введите допустимое значение!")

        elif userInput == 2:
            os = True
            while os:
                print("Введите исходные данные")
                kos = input("Kos = ")
                if kos.replace('.', '', 1).isdigit():
                    kos = float(kos)
                    wos = matlab.tf([kos, 0], [1])

                    os = False
                else:
                    print("Введите допустимое значение!")
        elif userInput == 3:
            os = True
            while os:
                print("Введите исходные данные")
                kos = input("Kos = ")
                tos = input("Tos = ")
                if kos.replace('.', '', 1).isdigit() and tos.replace('.', '', 1).isdigit():
                    kos = float(kos)
                    tos = float(tos)
                    wos = matlab.tf([kos], [tos, 1])

                    os = False
                else:
                    print("Введите допустимое значение!")
        elif userInput == 4:
            os = True
            while os:
                print("Введите исходные данные")
                kos = input("Kos = ")
                tos = input("Tos = ")
                if kos.replace('.', '', 1).isdigit() and tos.replace('.', '', 1).isdigit():
                    kos = float(kos)
                    tos = float(tos)
                    wos = matlab.tf([kos, 0], [tos, 1])

                    os = False
                else:
                    print("Введите допустимое значение!")
        else:
            print('Введите допустимое значение!')
            choiseOS = True
    else:
        print("Введите допустимое значение!")
w1 = wos
print(w1)

w2 = True
while w2:
    print("Введите исходные данные")
    tg = input("Tg = ")
    if tg.replace('.', '', 1).isdigit():
        tg = float(tg)
        wg = matlab.tf([1], [tg, 1])

        w2 = False
    else:
        print("Введите допустимое значение!")
w2 = wg
print(w2)

choiseTurbine = True
while choiseTurbine:
    userInput = input("Введите номер нужной турбины: \n"
                      "1 - Гидравлическая турбина \n"
                      "2 - Паровая турбина \n")
    if userInput.isdigit():
        choiseTurbine = False
        userInput = int(userInput)
        if userInput == 1:
            turbine = True
            while turbine:
                print("Введите исходные данные")
                tgt = input("Tgt = ")
                tg = input("Tg = ")
                if tgt.replace('.', '', 1).isdigit() and tg.replace('.', '', 1).isdigit():
                    tgt = float(tgt)
                    tg = float(tg)
                    wt = matlab.tf([0.01*tgt, 1], [0.05*tg, 1])
                    turbine = False
                else:
                    print("Введите допустимое значение!")

        elif userInput == 2:
            turbine = True
            while turbine:
                print("Введите исходные данные")
                kpt = input("Kpt = ")
                tpt = input("Tpt = ")
                if kpt.replace('.', '', 1).isdigit() and tpt.replace('.', '', 1).isdigit():
                    kpt = float(kpt)
                    tpt = float(tpt)
                    wt = matlab.tf([kpt], [tpt, 1])
                    turbine = False
                else:
                    print("Введите допустимое значение!")
        else:
            print('Введите допустимое значение!')
            choiseTurbine = True
    else:
        print("Введите допустимое значение!")
w3 = wt
print(w3)

w4 = True
while w4:
    print("Введите исходные данные")
    ky = input("Ky = ")
    ty = input("Ty = ")
    if ky.replace('.', '', 1).isdigit() and ty.replace('.', '', 1).isdigit():
        ky = float(ky)
        ty = float(ty)
        wy = matlab.tf([ky], [ty, 1])
        w4 = False
    else:
        print("Введите допустимое значение!")
w4 = wy
print(w4)

# Задаем размкнутую передаточную функцию
print("Разомкнутая передаточная функция")
w5 = w2*w3*w4
w55 = matlab.series(w3, w4, w2, w1)
print(w55)
# Задаем замкнутую передаточную функцию
print("Замкнутая передаточная функция")
w = matlab.feedback(w5, w1)
print(w)

time = []
for i in range(0, 2500):
    time.append(i/100)
# Строим переходную характеристику
pyplot.subplot()
pyplot.grid(True)
[y, x] = matlab.step(w, time)
pyplot.plot(x, y)
pyplot.title('Переходна характеристика')
pyplot.ylabel('Амплитуда')
pyplot.xlabel('Время')
pyplot.show()

# находим корни характеристичкского уравнения и определяем устойчивость системы
korny = matlab.pzmap(w)
pyplot.axis([-3, 1,-1, 1])
pyplot.show()
pole = matlab.pole(w)
print(pole)
deistv = []
for i in pole:
    kx = i.real
    deistv.append(kx)
if (min(deistv) > 0.0001):
    print("система неустйочива по корням характеристического уравнения")
elif (max(deistv) < -0.0001):
    print("система устойчива по корням характеристического уравнения")
else:
    print("система на границе устойчивости")

# Построение Диаграммы Найквиста и ЛЧХ
def graph(title):
    pyplot.subplot()
    pyplot.grid(True)
    if title == "Диаграмма Найквиста":
        nyquist = matlab.nyquist(w55)
        pyplot.title(title)
        pyplot.xlabel("Re")
        pyplot.ylabel("Im")
        pyplot.axis([-5, 20, -15, 5])
        pyplot.plot()
    elif title == "Логорифмические характеристики":
        mag, phase, omega = matlab.bode(w55)
        pyplot.plot()

graph("Диаграмма Найквиста")
pyplot.show()

graph("Логорифмические характеристики")
pyplot.show()

# Построение годогрофа Михайлова
v = symbols('v', real=True)  # равно омего
koef = w.den  # создаем массиф коэффициентов знаменателя
a = 1
uravnenie = 0
pole = []

for i in koef[0]:
    for b in i:
        n = len(i) - a # показатель степени (n-1)
        uravnenie = uravnenie + b * (I * v) ** n # производим замен p на jw
        a = a + 1
        pole.append(b)
print(uravnenie) # итоговое уравнение после замены переменной


wr = re(uravnenie)
wm = im(uravnenie)
print("Действительная часть = ", wr)
print("Мнимая часть = ", wm)
x = [wr.subs({v: q}) for q in numpy.arange(0, 100, 0.1)] # производим изменение частоты от 0 до 100
y = [wm.subs({v: q}) for q in numpy.arange(0, 100, 0.1)]
pyplot.axis([-40, 25, -10, 10])
pyplot.plot(x, y)
pyplot.grid(True)
pyplot.show()

# Определение предельного значения коэффициента обратнаой связи, при котором САУ теряет устойчивост
for kockrit in numpy.arange(0, 10, 0.001):
    koc = matlab.tf([kockrit], [1])
    wo = matlab.feedback(w5, koc)
    koef = wo.den[0][0]
    position = {}
    nomer = len(koef)
    for j in range(nomer):
        position["%s" % j] = koef[j]
    matrix = numpy.array([[position["1"], position["3"]], [position["0"], position["2"]]])
    if (numpy.linalg.det(matrix) >= -0.01) & (numpy.linalg.det(matrix) <= 0.02):
        print(matrix)
        print("определитель =", numpy.linalg.det(matrix))
        print("предел знач", kockrit)
        kocitog = kockrit

# Производим экспериментальную проверку предельного значения коэффициента обратной свзяи
wockrit = matlab.tf([kocitog], [1])
w = matlab.feedback(w5, wockrit)
print("Разомкнутая передаточная функция")
wraz = matlab.series(w3, w4, w2, wockrit)
print(wraz)
print("Замкнутая передаточная функция")
print(w)

pyplot.subplot()
pyplot.grid(True)
[y, x] = matlab.step(w, time)

pyplot.plot(x, y)
pyplot.title('Переходна характеристика')
pyplot.ylabel('Амплитуда')
pyplot.xlabel('Время')
pyplot.show()


korny = matlab.pzmap(w)
pyplot.axis([-3, 1,-1, 1])
pyplot.show()
pole = matlab.pole(w)
print(pole)
deistv = []
for i in pole:
    kx = i.real
    deistv.append(kx)
if (min(deistv) > 0.0001):
    print("система неустйочива по корням характеристического уравнения")
elif (max(deistv) < -0.0001):
    print("система устойчива по корням характеристического уравнения")
else:
    print("система на границе устойчивости")

def graph(title):
    pyplot.subplot()
    pyplot.grid(True)
    if title == "Диаграмма найквеста":
        nyquist = matlab.nyquist(wraz)
        pyplot.title(title)
        pyplot.xlabel("Re")
        pyplot.ylabel("Im")
        pyplot.axis([-10, 40, -25, 5])
        pyplot.plot()

    elif title == "Логорифмические характеристики":
        mag, phase, omega = matlab.bode(wraz)
        pyplot.plot()

graph("Диаграмма найквеста")
pyplot.show()

graph("Логорифмические характеристики")
pyplot.show()

koef = w.den  # создаем массиф коэффициентов знаменателя
a = 1
uravnenie = 0
pole = []

for i in koef[0]:
    for b in i:
        n = len(i) - a # показатель степени (n-1)
        uravnenie = uravnenie + b * (I * v) ** n # производим замен p на jw
        a = a + 1
        pole.append(b)
print(uravnenie) # итоговое уравнение после замены переменной


wr = re(uravnenie)
wm = im(uravnenie)
print("Действительная часть = ", wr)
print("Мнимая часть = ", wm)
x = [wr.subs({v: q}) for q in numpy.arange(0, 100, 0.1)] # производим изменение частоты от 0 до 100
y = [wm.subs({v: q}) for q in numpy.arange(0, 100, 0.1)]
pyplot.axis([-40, 40, -20, 10])
pyplot.plot(x, y)
pyplot.grid(True)
pyplot.show()
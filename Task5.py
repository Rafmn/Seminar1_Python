# Задача 5: Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

x1 = int(input('Введите значение х для первой точки: '))
y1 = int(input('Введите значение у для первой точки: '))
x2 = int(input('Введите значение х для второй точки: '))
y2 = int(input('Введите значение у для второй точки: '))

ab = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


print('Расстояние между двумя точками:', ab)
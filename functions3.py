# В зависимости от выбора пользователя, вычислить площадь круга,
# прямоугольника или треугольника. Для вычисления площади каждой
# фигуры должна быть написана отдельная функция.
import math
def area(r):
    area = r ** 2 * math.pi
    return area
def priam (a,b):
    return a*b
def treug (a,b,c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p-a) * (p-b) * (p-c))
s = input("Выберите фигуру для вычисления площади : Круг, прямоугольник или треугольник: ")
if s == 'круг':
    r = float(input("Радиус: "))
    print("Площадь круга: ", area(r))
elif s == 'прямоугольник':
    l = float(input("Длина: "))
    w = float(input("Ширина: "))
    print("Площадь прямоугольника: ",priam(l,w))
elif s == 'треугольник':
    AB = float(input("Первая сторона: "))
    BC = float(input("Вторая сторона: "))
    CA = float(input("Третья сторона: "))
    print("Площадь треугольника: ", treug(AB,BC,CA))

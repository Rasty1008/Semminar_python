'''
Напишите программу, которая принимает на вход координаты точки (X и Y),
причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

Пример:
- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3
'''

def input_coordinates(x):
    input_coord = [0] * x
    for i in range(x):
        status = False
        while not status:
            try:
                number = float(input(f"Введите {i+1} координату: "))
                input_coord[i] = number
                status = True
                if input_coord[i] == 0:
                    status = False
                    print("Не равна 0!")
            except ValueError:
                print("Ввод только в числах!")
    return input_coord

def coordinates(xy):
    a = 4
    if xy[0] > 0 and xy[1] > 0:
        a = 1
    if xy[0] < 0 and xy[1] > 0:
        a = 2
    if xy[0] < 0 and xy[1] < 0:
        a = 3
    print(f"Точка  {a} в четветрой плоскости")

    coordinate_xy = input_coordinates()
    coordinates(coordinate_xy)



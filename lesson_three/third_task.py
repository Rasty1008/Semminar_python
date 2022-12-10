'''
Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
Пример
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''

input_lst = [float(number) for number in input("Введите числа через пробел: ").split()]
print(f"список чисел: {input_lst}")


def difference(lst):
    new_lst = [round(i % 1,2) for i in lst if i % 1 != 0]
    return max(new_lst) - min(new_lst)


print(difference(input_lst))

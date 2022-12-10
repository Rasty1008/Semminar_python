'''
Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
'''
input_lst = [int(number) for number in input("Введите числа через пробел: ").split()]
print(input_lst)


def multiplication(lst):
    l = len(lst) // 2 + 1 if len(lst) % 2 != 0 else len(lst) // 2
    new_lst = [lst[i] * lst[len(lst) - i - 1] for i in range(l)]
    return new_lst

print(multiplication(input_lst))


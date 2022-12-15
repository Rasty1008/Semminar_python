'''
Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
*Пример*
- при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]
'''

input_lst = list(map(int, input("Введите числа через пробел:\n").split()))
print(input_lst)
new_list = []
for i in input_lst:
    if  i not in new_list:
        new_list.append(i)
print(new_list)
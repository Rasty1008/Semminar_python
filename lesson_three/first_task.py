'''
Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''
input_list = [int(number) for number in input("Введите список чисел через пробел: ").split()]
print("Список чисел:", input_list)

def result(lst):
    answer = 0
    for i in range(len(lst)):
        if i % 2 != 0:
            answer += lst[i]
    return answer

print(f"Сумма элементов списка: {result(input_list)}")

    

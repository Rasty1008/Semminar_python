'''
1 Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10
'''

number = int(input("Введите число: "))

bin_number = lambda x: bin(x).replace("0b", "")
print(bin_number(number))


'''
2 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''
input_list = list(map(int, input("Введите число через пробел: ").split()))
print("Список чисел:", input_list)


def result(lst):
    answer = 0
    for i in range(len(lst)):
        if i % 2 != 0:
            answer += lst[i]
    return answer

print(f"Сумма элементов списка: {result(input_list)}")


'''
3 Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
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

'''
4 Напишите программу, удаляющую из файла все слова, содержащие "абв"
'''

def write_file(res):
    with open('file_text.txt', 'w') as data:
        data.write(res)

def del_symbols(file):
    file = list(filter(lambda x: 'абв' not in x, file.split()))
    return " ".join(file)

txt = "абв Напишите абв программу, абв удаляющую из файла абв все слова, абв содержащие \"абв\""
#res_text = del_symbols(txt)
#print(write_file(res_text))
write_file(del_symbols(txt))


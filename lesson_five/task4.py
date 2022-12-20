'''
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах.

aaaasssdddwwwwwwwwwwwweeeffffff -> 4a3s3d9w3w3e6f
4a3s3d9w3w3e6f-> aaaasssdddwwwwwwwwwwwweeeffffff
'''


def code(text):
    count = 1
    res = ''
    for i in range(len(text) - 1):
        if text[i] == text [i + 1]:
            count += 1
        else:
            res = res + str(count) + text[i]
            count = 1
    if count > 1 or (text[len(text) - 2] != text[-1]):
        res = res + str(count) + text[-1]
    return res

def dec(text):
    number = ''
    res = ''
    for i in range(len(text)):
        if not text[i].isalpha():
            number += text[i]
        else:
            res = res + text[i] * int(number)
            number = ''
    return res

input_ = input("Введите текст: ")
print(f"Текст после кодировки: {code(input_)}")
print(f"Текст после дештфровки: {dec(code(input_))}")
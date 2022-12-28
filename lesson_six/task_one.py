'''
Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10
'''

number = int(input("Введите число: "))

bin_number = lambda x: bin(x).replace("0b", "")
print(bin_number(number))



'''
bin_ = ''
while number > 0:
    bin_ = str(number % 2) + bin_
    number = number // 2

print(bin_)
'''
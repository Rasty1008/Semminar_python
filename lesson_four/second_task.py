'''
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
*Пример*
- при N=236     ->        [2, 2, 59]
'''
input_number = int(input("Введите число: "))
i = 2
lst = []
number = input_number
while i <= number:
    if number % i == 0:
        lst.append(i)
        number //= i
        i = 2
    else:
        i += 1
print(f"Множетели числа: {number} в списке: {lst}")
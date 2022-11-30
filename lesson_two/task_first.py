'''Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
*Пример:*
- 6782 -> 23
- 0.56 -> 11'''

def input_number(text):
    input_text = False
    while not input_text:
        try:
            number = float(input(f"{text}"))
            input_text = True
        except ValueError:
            print("Введите число!")
    return number

def number_sum(numb):
    sum = 0
    for i in str(numb):
        if i != ".":
            sum += int(i)
    return sum

numbers = input_number("Введите число: ")
print(f"Сумма чисел равна: {number_sum(numbers)}")


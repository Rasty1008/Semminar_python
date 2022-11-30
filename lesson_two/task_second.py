'''Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
*Пример:*
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)'''

def input_number(text):
    input_text = False
    while not input_text:
        try:
            number = int(input(f"{text}"))
            input_text = True
        except ValueError:
            print("Введите число!")
    return number

def factorial(n):
    number = 1
    for i in range(1, n + 1):
        number *= i
    return number

number = input_number("Введите число: ")

factorial_list = []
for i in range(1, number + 1):
    factorial_list.append(factorial(i))

print(f"Факториал числа равен: {factorial_list}")
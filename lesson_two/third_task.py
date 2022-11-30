'''Задайте список из n чисел последовательности (1 + 1 / n)**n и выведите на экран их сумму.
*Пример:*
- Для n = 6: [2.0, 2.25, 2.37, 2.44, 2.488, 2.52]     ->       14.072 '''

n = int(input("Введите число: "))
lst = [round((1 + 1 / i)**i, 3) for i in range(1, n + 1)]
print(f"Последовательность чисел: {lst}\nСумма: {round(sum(lst), 3)}")
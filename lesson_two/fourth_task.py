'''4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
 Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.'''

array = [int(input("Введите элемент: ")) for i in range(int(input("Введите длину списка: ")))]

prod = 1
for i in array:
    prod *= 1

print(f"Список: {array}")
print(f"Сумма элементов списка: {sum(array)}")
print(f"Произведение элементов списка: {prod}")
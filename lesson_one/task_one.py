'''
Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
Пример:
- 6 -> да
- 7 -> да
- 1 -> нет
'''

def possible_error(text):
    pos_text = False
    while not pos_text:
        try:
            number = int(input(f"{text}"))
            pos_text = True
        except ValueError:
            print('Не является числом!')
    return number        

def day_of_the_week(number):
    if number >= 6 and number <= 7:
        print('Definitely yes')
    elif number < 6 and number > 0:
        print('NO')
    else:
        print('В неделе семь дней!')

input_number = int(input('Enter the number: '))
day_of_the_week(input_number)
'''
Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета.
Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой.
За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход.
Сколько конфет нужно взять первому игроку, чтобы забрать все
конфеты у своего конкурента?

a) Добавьте игру против бота
b) Подумайте как наделить бота "интеллектом"
'''
from random import randint

def input_players(count):
    x = int(input(f"{count}, введите кол-во конфет, от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{count}, введите кол-во от 1 до 28: "))
    return x

def print_(name, candy, amount, candys):
    print(f"Игрок {name}, он взял {candy}, кол-во конфет у него {amount}. Осталось {candys}")

player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
candys = int(input("Введите кол-во конфет на столе: "))
turn = randint(0,2) #очередь игроков
if turn:
    print(f"Первый ходит игрок {player1}")
else:
    print(f"Первый ходит игрок {player2}")
counter1 = 0
counter2 = 0
while candys > 28:
    if turn:
        candy = input_players(player1)
        counter1 += candy
        candys -= candy
        turn = False
        print_(player1, candy, counter1, candys)
    else:
        candy = input_players(player2)
        counter2 += candy
        candys -= candy
        turn = True
        print_(player2, candy, counter2, candys)
    
if turn:
    print(f"Выиграл {player1}")    
else:
    print(f"Выйграл {player2}")




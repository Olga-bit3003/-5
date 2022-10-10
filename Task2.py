from curses.ascii import isdigit
import random


def start():
    print(f'Добро пожаловать в игру')
    print(f'На столе лежит 2021 конфета')
    print(f'Играют два игрока делая ход друг после друга')
    print(f'С тобой будет играть БОТ')
    print(f'Первый ход определим жеребьёвкой')
    print(f'За один ход можно забрать не более чем 28 конфет')
    print(f'Все конфеты  достаются сделавшему последний ход')
    print(f'')



def rnd_turn():
    print(f'Выбор очередности ходов: ')
    print(f'Введите enter, чтобы выбрать очередность ходов случайным образом')
    while True:
        n = input('> ')
        if n.isdigit():
            n = int(n)
            n = random.randint()
               
            print(f'Первым будет ходить игрок!')
        else:
            print(f'Первым будет ходить компьютер!')
            break
        
    return n


def turn_player(matches):
    n = 28
    while n > 28 or n < 1:
        n = input('Сколько вы возьмете Конфет? ')
        if n.isdigit():
            n = int(n)
            if n > 28 or n < 1:
                print(f'Вы вязли недопустимое количества ! Возьмите от 1 до 28')
            if n > matches:
                print(f'Вы взяли больше чем осталось!')
                n = 28
        else:
            print(f'Вы ввели недопустимые символы. Введите число от 1 до 28')
            n = 28
    return n

def turn_ai(matches):
    n = matches % 5
    if n == 0:
        n = random.randint(1, 28)
    return n

matches = 2021
count = 2
start()
turn = matches
while True:
    print(f'\n Ход номер: {count} ')
    if turn % 2 == 0:
        print(f'Ход игрока! Всего : {matches}')
        n = turn_player(matches)
        print(f'Игрок взял : {n}')
    elif turn % 2 == 1:
        print(f'Ход компьютера! Всего: {matches}')
        n = turn_ai(matches)
        print(f'Компьютер взял : {n}')
    matches -= n
    if matches == 0:
        if turn % 2 == 0:
            print(f'Победил игрок!')
        else:
            print(f'Победил компьютер!')
        break
    turn += 1
    count += 1

print('\n'*5)
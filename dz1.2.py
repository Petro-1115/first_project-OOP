from random import randint, random

print('--== Вас приветствует игра Угадай число')

attempts = 0
num = randint(1,10)
print('Я загадал число от 1 до 10! Попробуешь угадать?')
print('У тебя есть 4 попытки!')

while attempts < 4:
    choose = int(input('Введите число:'))

    attempts += 1

    if choose > num:
        print('Твоё число больше моего!')

    if choose < num:
        print('Твоё число меньше моего!')

    if choose == num:
        break

if choose == num:
    print('Поздравляю! Ты отгадал загаданное число.')
else:
    print('К сожалению, ты не смог, попробуй ещё раз!')




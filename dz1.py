print('-= Вас приветствует калькулятор =-')

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
choose = input('Введите действие: (1 - Сложение; 2 - Вычетание; 3 - Умножение; 4 - Деление;)')
result = 0

if choose == '1':
    print(a + b)

if choose == '2':
    print(a - b)

if choose == '3':
    print(a * b)

if choose == '4' and b == 0:
    print('Действие невозможно')
else:
    print(a / b)

if choose != 1 or 2 or 3 or 4:
    print('Такого действия не существует')
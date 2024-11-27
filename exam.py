import sqlite3

connection = sqlite3.connect("db2.sl3", 5)
cur = connection.cursor()

#cur.execute("CREATE TABLE exam (login TEXT, password TEXT);")
#connection.commit()


choice = int(input('Выберите действие: 1 - Войти, 2 - Зарегестрироваться: '))
if choice == 2:
    print('---Регистрация---')
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    cur.execute(f"SELECT rowid FROM exam WHERE login='{login}';")
    res = cur.fetchall()
    if res != []:
        print('Данный логин уже занят!')
    else:
        cur.execute(f"INSERT INTO exam (login, password) VALUES ('{login}', '{password}');")
        connection.commit()
        print('Данные добавлены')
elif choice == 1:
    print('---Авторизация---')
    log = input('Введите логин: ')
    passwd = input('Введите пароль: ')
    cur.execute(f"SELECT rowid FROM exam WHERE login='{log}';")
    res = cur.fetchall()
    if res != []:
        print('Вход успешный')
    if res == []:
        print('Пользователь не существует')
#cur.execute(f"DELETE FROM exam WHERE rowid=15;")
#connection.commit()



connection.close()
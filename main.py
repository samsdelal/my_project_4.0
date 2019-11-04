import random as r
import local as lc
import string
from prettytable import PrettyTable #Для установки данной библиоткеи введите в terminal 'easy_install prettytable'

table = PrettyTable(['Количество', 'Сгенерированные пароли'])
time = 0
x = int(input('Здравствуйте, сгенерировать вам простой пароль ?\n'
              '\n'
              '1. [Да]\n'
              '2. [Нет]\n'
              '\n'
              '------ '))
while x != 2:
    year = input('Введите свой год рождения - ')
    print(lc.TXT_SKIP)
    month = input('Введите свой месяц рождения (слово, а не число)- ')
    print(lc.TXT_SKIP)
    day = input('Ввелите свой день рождения - ')
    print(lc.TXT_SKIP)
    name = input('Введите свое имя - ')
    print(lc.TXT_SKIP)
    fam = input('Введите свою фамилию - ')
    print(lc.TXT_SKIP)

    PASS1 = year[(r.randint(0, (len(year) - 1)))]
    PASS2 = month[(r.randint(0, (len(month)-1)))]
    PASS3 = day[(r.randint(0, (len(day)-1)))]
    PASS4 = name[(r.randint(0, (len(name)-1)))]
    PASS5 = fam[(r.randint(0, (len(fam)-1)))]
    PASS6 = r.choice(string.ascii_letters)
    PASS7 = r.choice(string.ascii_uppercase)

    passwd = PASS1 + PASS2 + PASS3 + PASS7 + PASS4 + PASS5 + PASS6
    time += 1
    table.add_row([time, passwd])
    print(passwd)

    x = int(input("Сгенерировать вам еще один простой пароль ?\n"
                  "\n"
                  "1. [Да]\n"
                  "2. [Нет]\n"
                  "\n"
                  "------ "))

else:
    print(table)

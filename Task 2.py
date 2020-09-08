# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def personal_info(**kwargs):
    return list(kwargs.values())


def personal_info_input():
    print(personal_info(name=input('Enter Name: '),
                        s_name=input('Enter Surname: '),
                        b_date=input('Enter Birth Date: '),
                        l_town=input('Enter Live Town: '),
                        email=input('Enter E-mail: '),
                        tel=input('Enter Tel.number: ')))


print(personal_info_input())

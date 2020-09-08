# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

arg_1 = int(input('Enter dividend: '))
arg_2 = int(input('Enter divider: '))

def div(*args):
    try:
        res = arg_1 / arg_2
    except ValueError:
        return 'Value Error'
    except ZeroDivisionError:
        return 'Zero Division Error'
    return res

print(div())

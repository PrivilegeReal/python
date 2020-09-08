# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
# аргументов.

arg_1 = int(input('Enter first argument value: '))
arg_2 = int(input('Enter second argument value: '))
arg_3 = int(input('Enter third argument value: '))

def arg_ops(**z):
    z = [arg_1, arg_2, arg_3]
    z.remove(min(arg_1, arg_2, arg_3))
    return sum(z)

print(arg_ops())

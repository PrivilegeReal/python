# 2. Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

elements_count = int(input('Введите количество элементов списка: '))
user_list = []
i = 0
elements = 0

while i < elements_count:
    user_list.append(input('Введите следующее значение списка: '))
    i += 1

for el in range(int(len(user_list) / 2)):
    user_list[elements], user_list[elements + 1] = user_list[elements + 1], user_list[elements]
    elements += 2
print(user_list)

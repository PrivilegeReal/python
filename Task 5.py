# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

rating_list = [10, 8, 5, 4, 4, 1]
print(f'Рейтинг: {rating_list}')
user_digit = int(input('Для выхода из редактирования листа рейтинга введите `743`. Введите рейтинговое число: '))
while user_digit != 743:
    for el in range(len(rating_list)):
        if rating_list[el] == user_digit:
            rating_list.insert(el + 1, user_digit)
            break
        elif rating_list[0] < user_digit:
            rating_list.insert(0, user_digit)
        elif rating_list[-1] > user_digit:
            rating_list.append(user_digit)
        elif rating_list[el] > user_digit > rating_list[el + 1]:
            rating_list.insert(el + 1, user_digit)
    print(f'текущий список - {rating_list}')
    user_digit = int(input('Введите число '))

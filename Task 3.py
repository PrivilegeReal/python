# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

seasons_list = ['winter month', 'spring month', 'summer month', 'autumn month']
seasons_dictionary = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}
month = int(input('Укажите порядковый номер месяца: '))
if month == 1 or month == 12 or month == 2:
    print(seasons_dictionary.get(1))
    print(seasons_list[0])
elif month == 3 or month == 4 or month == 5:
    print(seasons_dictionary.get(2))
    print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons_dictionary.get(3))
    print(seasons_list[2])

elif month == 9 or month == 10 or month == 11:
    print(seasons_dictionary.get(4))
    print(seasons_list[3])
else:
    print('What an inventor! There are 12 of them in the calendar!')

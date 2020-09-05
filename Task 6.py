# * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
# информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (
# характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно,
# т.е. запрашивать все данные у пользователя. Пример готовой структуры:
# [ (1, {“название”: “компьютер”, # “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2,# “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”}) ]

# Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров. Пример:
# { “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7], “ед”: [“шт.”] }

ware = []
parameters = {'name': '', 'price': '', 'quantity': '', 'unit': ''}
ware_analytics = {'name': [], 'price': [], 'quantity': [], 'unit': []}
num = 0
ware_parameter = None
command = None

while True:
    command = input('For close app input "Quit", for continue press "Enter", for analytics input "Ant" ').upper()
    if command == 'QUIT':
        print('The app will be closed.')
        break
    num += 1
    if command == 'ANT':
        print(f'Current analytics\n {"-" * 30}')
        for key, value in ware_analytics.items():
            print(f'{key[:25]:>30}: {value}')
            print("-" * 30)
    for el in parameters.keys():
        ware_parameter = input(f'Input parameter "{el}"')
        parameters[el] = int(ware_parameter) if (el == 'price' or el == 'quantity') else ware_parameter
        ware_analytics[el].append(parameters[el])
    ware.append((num, parameters))


# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

user_str = input('Введите строку, содержащую произвольное количество элементов, разделенных пробелом: ')
user_word = []
string_num = 1
for el in range(user_str.count(' ') + 1):
    user_word = user_str.split()
    if len(str(user_word)) <= 10:
        print(f' {string_num} {user_word[el]}')
        string_num += 1
    else:
        print(f' {string_num} {user_word[el][0:10]}')
        string_num += 1

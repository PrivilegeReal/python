# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить ее на экран.

def summary():
    try:
        with open('task5.txt', 'w') as f:
            line = input('Ведите числа через пробел: \n')
            f.writelines(line)
            user_nums = line.split()

            print(sum(map(int, user_nums)))
    except IOError:
        print('IOError')
    except ValueError:
        print('Ну и как мне Это просуммировать!? Вводите Числа!')

summary()

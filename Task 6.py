# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого
# предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему. Вывести словарь на экран. Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб) Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

my_lessons = {}
with open('task6.txt') as f:
    lines = f.readlines()
    for line in lines:
        splitted_line = line.split()
        lesson = splitted_line[0]
        lessons_hours = sum([int(x[:x.find('(')]) for x in splitted_line[1:] if '(' in x])
        my_lessons[lesson[:-1]] = lessons_hours
print(my_lessons)

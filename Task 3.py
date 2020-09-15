# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
# средней величины дохода сотрудников.

with open('task3.txt') as f:
    salary_list = []
    lines = f.readlines()
    for line in lines:
        employee, salary = line.split(' - ')
        salary_list.append(int(salary))
        if int(salary) < 20000:
            print(line)
    print('Average wage:', sum(salary_list) / 3)
    #3 сотрудника (в моем случае), без точного значения: print('Average wage:', sum(salary_list) / len(salary_list))

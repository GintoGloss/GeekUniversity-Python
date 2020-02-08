# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
# средней величины дохода сотрудников.


with open('employees.txt', encoding='utf-8') as f:
    lines = f.readlines()
avg_wage = 0.0
for line in lines:
    line = line.split()
    employee = line[0]
    wage = float(line[1])
    if wage < 20000.0:
        print(employee)
    avg_wage += wage
if len(lines) > 0:
    avg_wage = avg_wage / len(lines)
print("Средний доход =", avg_wage)

# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
# фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее
# сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

try:
    revenue = int(input("Введите выручку в натуральном выражении: "))
    cost = int(input("Введите издержки в натуральном выражении: "))
    if revenue <= 0 or cost <= 0:
        raise ValueError
except ValueError:
    print("Неверный ввод!")
else:
    profit = revenue - cost
    if profit == 0:
        print("Фирма работает в ноль")
    elif profit < 0:
        print("Фирма терпит убытки")
    else:
        print("Фирма работает с прибылью", profit)
        profit_margin = profit / revenue
        print("Рентабельность выручки =", profit_margin)
        employee_count = input("Введите число работников фирмы: ")
        if (not employee_count.isdecimal()) or int(employee_count) == 0:
            print("Неверный ввод!")
        else:
            profit_per_employee = profit / int(employee_count)
            print("Прибыль фирмы в расчете на одного сотрудника:", profit_per_employee)

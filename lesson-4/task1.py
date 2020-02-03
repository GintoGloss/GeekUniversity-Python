# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
# необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных
# значений необходимо запускать скрипт с параметрами.


from sys import argv
try:
    script_name, hours, wage, bonus = argv
    hours = float(hours)
    wage = float(wage)
    bonus = float(bonus)
    if hours < 0 or wage <= 0 or bonus < 0:
        raise ValueError
except ValueError:
    print("Ошибка ввода")
else:
    print("Заработная плата =", hours * wage + bonus)

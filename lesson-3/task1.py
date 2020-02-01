# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
# пользователя, предусмотреть обработку ситуации деления на ноль.


def divide(arg1, arg2):
    """Возвращает результат деления, с обработкой ситуации деления на ноль"""
    return None if arg2 == 0 else arg1 / arg2


while True:
    dividend = input("Введите делимое: ")
    divisor = input("Введите делитель: ")
    try:
        dividend = float(dividend)
        divisor = float(divisor)
    except ValueError:
        print("Принимаются только числа!")
    else:
        break

result = divide(dividend, divisor)
print("На ноль делить нельзя!") if result is None else print("Частное:", result)

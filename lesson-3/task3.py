# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
# аргументов.


def my_func(arg1, arg2, arg3):
    """Возвращает сумму двух наибольших численных аргументов"""
    try:
        arg1 = float(arg1)
        arg2 = float(arg2)
        arg3 = float(arg3)
    except ValueError:
        return None
    else:
        return arg1 + arg2 + arg3 - min(arg1, arg2, arg3)


a = input("Введите число: ")
b = input("Введите число: ")
c = input("Введите число: ")
print(my_func(a, b, c))

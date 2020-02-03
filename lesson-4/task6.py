# 6. Реализовать два небольших скрипта:
# а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
# б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.


from itertools import count, cycle


def script_a(number, stopper):
    if type(number) != int or type(stopper) != int:
        return ValueError
    for el in count(number):
        if el > stopper:
            break
        else:
            print(el)
    return 1


def script_b(my_list, stopper):
    if type(my_list) != list or type(stopper) != int:
        return ValueError
    i = 0
    for el in cycle(my_list):
        if i > stopper:
            break
        print(el)
        i += 1
    return 1


script_a(10, 21)
script_b([1, 2, 3, 4, 5], 11)
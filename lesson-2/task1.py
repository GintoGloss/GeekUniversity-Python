# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных
# каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у
# пользователя, а указать явно, в программе.

my_list = ["one", 2, 3.0, False, (1, 2, 3), "element", [1, "2"]]

for el in my_list:
    print(type(el))

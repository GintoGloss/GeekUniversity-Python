# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего
# элемента. Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка
# использовать генератор.


my_list = [1, 0, 1, 2, 1, 3, 2, 3, 4, 4, 5]
new_list = [el for index, el in enumerate(my_list) if el > my_list[index - 1]]
print(new_list)
# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел,
# соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения задания
# обязательно использовать генератор.


my_list = [1, 1, 2, 3, 3, 4, 5, 6, 5]
new_list = [el1 for el1 in my_list if len([el2 for el2 in my_list if el1 == el2]) == 1]
print(new_list)
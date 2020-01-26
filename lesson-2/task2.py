# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и
# 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка
# элементов необходимо использовать функцию input().

my_list = []
list_len = input("Сколько элементов хотите ввести? ")
while (not list_len.isdecimal()) or int(list_len) == 0:
    list_len = input("Нужно ввести натуральное число! ")
list_len = int(list_len)

while len(my_list) < list_len:
    my_list.append(input("#"))
print(my_list)

for index, elem in enumerate(my_list):
    if index % 2 == 0 and index < len(my_list) - 1:
        my_list[index], my_list[index + 1] = my_list[index + 1], my_list[index]
print(my_list)

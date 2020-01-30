# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя
# необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

rating_list = [7, 5, 3, 3, 2]
rating_len = len(rating_list)

new_elem = input("Введите новый элемент рейтинга: ")
while (not new_elem.isdecimal()) or int(new_elem) == 0:
    new_elem = input("Нужно ввести натуральное число! ")
new_elem = int(new_elem)

for index, elem in enumerate(rating_list[::-1]):
    if elem >= new_elem:
        rating_list.insert(rating_len - index, new_elem)
        break
if len(rating_list) == rating_len:
    rating_list.insert(0, new_elem)

print(rating_list)

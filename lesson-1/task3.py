# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3
# + 33 + 333 = 369.

number = input("Введите натуральное число: ")
if (not number.isdecimal()) or int(number) == 0:
    print("Неверный ввод!")
else:
    number = int(number) + int(number + number) + int(number + number + number)
    print(number)
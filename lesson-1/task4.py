# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл
# while и арифметические операции.

number = input("Введите натуральное число: ")
if (not number.isdecimal()) or int(number) == 0:
    print("Неверный ввод!")
else:
    max_digit = 0
    number = int(number)
    while number > 9:
        current_digit = number % 10
        number //= 10
        if current_digit > max_digit:
            max_digit = current_digit
    if number > max_digit:
        max_digit = number
    print(max_digit)

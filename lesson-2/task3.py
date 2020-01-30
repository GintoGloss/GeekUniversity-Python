# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима,
# весна, лето, осень). Напишите решения через list и через dict


def seasons_with_list(number):
    seasons_list = [
        "Зима", "Зима", "Весна", "Весна", "Весна", "Лето", "Лето", "Лето",
        "Осень", "Осень", "Осень", "Зима"
    ]
    return seasons_list[number - 1]


def seasons_with_dict(number):
    seasons_dict = {
        1: "Зима", 2: "Зима", 12: "Зима", 3: "Весна", 4: "Весна", 5: "Весна", 6: "Лето", 7: "Лето",
        8: "Лето", 9: "Осень", 10: "Осень", 11: "Осень"
    }
    return seasons_dict.get(number)


number = input("Введите номер месяца: ")
if not number.isdecimal() or int(number) < 1 or int(number) > 12:
    print("Нет такого месяца!")
else:
    print("Время года", seasons_with_dict(int(number)))
    print("Время года", seasons_with_list(int(number)))

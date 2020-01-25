# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time = input("Введите время в секундах: ")
if not time.isdecimal():
    print("Неверный ввод!")
else:
    time = int(time)
    seconds = time % 60
    time //= 60
    minutes = time % 60
    hours = time // 60
    print(str.format("Ваше форматированное время {:02d}:{:02d}:{:02d}", hours, minutes, seconds))

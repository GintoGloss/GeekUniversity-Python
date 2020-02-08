# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить ее на экран.


with open('numbers.txt', 'w+') as f:
    is_writing = True
    while is_writing:
        new_string = input('> ')
        new_string = new_string.split()
        for num in new_string:
            try:
                float(num)
            except ValueError:
                is_writing = False
                break
            else:
                f.write(num + ' ')
    f.seek(0)
    total = 0
    for number in f.read().split():
        total += float(number)
    print(total)

# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться
# сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь
# введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
# выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить
# сумму этих чисел к полученной ранее сумме и после этого завершить программу.


def get_sum(string):
    """Возвращает сумму всех встреченных в строке чисел, разделенных через пробел, до первого встреченного не-числа"""
    if type(string) != str:
        return None
    string = str(string).split()
    sum = 0
    stop = 0
    for word in string:
        try:
            sum += float(word)
        except ValueError:
            stop = 1
            break
    return sum, stop


total = 0
while True:
    sum, stop = get_sum(input(">: "))
    total += sum
    print(total)
    if stop == 1:
        break

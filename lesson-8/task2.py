# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.


class MyException(Exception):

    err_text = 'Делитель не может быть равен 0!'

    def __init__(self):
        pass


number = 100
try:
    divider = int(input('Введите делитель: '))
    if divider == 0:
        raise MyException
except ValueError:
    print('Нужно ввести число!')
except MyException:
    print(MyException.err_text)
else:
    print(number / divider)

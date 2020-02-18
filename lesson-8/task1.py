# 1.1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных
# данных.


class Date:

    def __init__(self, string):
        self.day, self.month, self.year = Date.from_string(string)
        if not Date.is_valid(self.day, self.month, self.year):
            raise ValueError

    @classmethod
    def from_string(cls, string):
        day, month, year = map(int, string.split('-'))
        return day, month, year

    @staticmethod
    def is_valid(day, month, year):
        if year < 1 or month < 1 or day < 1 or month > 12 or day > 31:
            return False
        elif month == 2:
            if year % 4 != 0 and day > 28:
                return False
            elif day > 29:
                return False
        elif month == 4 or month == 6 or month == 9 or month == 11:
            if day > 30:
                return False
        return True


try:
    my_date = Date('29-2-2020')
    # my_date = Date('33-10-2002')
    # my_date = Date('13-13-2101')
    # my_date = Date('16-4-0')
    # my_date = Date('30-2-2020')
    # my_date = Date('29-2-2021')
except ValueError:
    print("Date is invalid!")
else:
    print(my_date.day)
    print(my_date.month)
    print(my_date.year)

# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс
# «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер,
# сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках
# реализовать параметры, уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а
# также других данных, можно использовать любую подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.


class ItemError(Exception):
    pass


class ItemCountError(Exception):
    pass


class Item:

    def __init__(self, obj, count):
        self.obj = obj
        self.count = count

    def __str__(self):
        return f'{self.obj} - {self.count}ед.'

    def __add__(self, other):
        result = self.count + other.count
        return Item(self.obj, result)

    def __sub__(self, other):
        result = self.count - other.count
        if result < 0:
            raise ItemCountError
        return Item(self.obj, result)


class Warehouse:

    def __init__(self, name):
        self.name = name
        self.content = {}

    def __str__(self):
        string = f'Содержимое склада {self.name}:\n--------\n'
        for item in self.content.values():
            string += f'{item}\n'
        return string

    def accept(self, ware, count):
        try:
            if not isinstance(count, int) or count < 1:
                raise ItemError
            new_item = Item(ware, count)
            key = str(ware)
            if key in self.content.keys():
                self.content[key] += new_item
            else:
                if not isinstance(ware, OfficeAutomation):
                    raise ItemError
                self.content[key] = new_item
        except ItemError:
            print('Введена неверная информация, техника не принята!')
        else:
            print(f'{new_item} принято на склад {self.name}')

    def send(self, ware, count, destination):
        try:
            if count < 1:
                raise ItemError
            new_item = Item(ware, count)
            key = str(ware)
            if key in self.content.keys():
                self.content[key] -= new_item
            else:
                raise ItemCountError
        except ItemError:
            print('Введена неверная информация, отправка техники не состоялась!')
        except ItemCountError:
            print('На складе недостаточно указанной техники, отправка не состоялась!')
        else:
            print(f'{new_item} отправлено в {destination}')


class OfficeAutomation:

    def __init__(self, model, manufacturer, paper_format):
        self.suffix = 'Оргтехника'
        self.model = model
        self.manufacturer = manufacturer
        self.paper_format = paper_format

    def __str__(self):
        return f"{self.suffix} {self.manufacturer} {self.model}"


class Printer(OfficeAutomation):

    def __init__(self, model, manufacturer, paper_format, print_technology):
        super().__init__(model, manufacturer, paper_format)
        self.suffix = 'Принтер'
        self.print_technology = print_technology

    def __str__(self):
        return super().__str__()


class Scanner(OfficeAutomation):

    def __init__(self, model, manufacturer, paper_format, dpi):
        super().__init__(model, manufacturer, paper_format)
        self.suffix = 'Сканер'
        self.dpi = dpi

    def __str__(self):
        return super().__str__()


class Copier(Scanner):

    def __init__(self, model, manufacturer, paper_format, dpi, copies_per_min):
        super().__init__(model, manufacturer, paper_format, dpi)
        self.suffix = 'Копир'
        self.copies_per_min = copies_per_min

    def __str__(self):
        return super().__str__()


my_warehouse = Warehouse('Главный')
printer = Printer('HL-L5100DN', 'Brother', 'A4', print_technology="Лазерный")
scanner = Scanner('ScanJet 7500', 'HP', 'A4', dpi=800)
my_warehouse.accept(printer, 3)
my_warehouse.accept('Принтер Brother HL-L5100DN', 2)
my_warehouse.accept(scanner, 4)
my_warehouse.send(printer, 2, 'Бухгалтерия')
my_warehouse.send('Принтер Brother HL-L5100DN', 2, 'Отдел Кадров')
my_warehouse.send(scanner, 2, 'Отдел Кадров')
print(my_warehouse)
print(my_warehouse.content['Принтер Brother HL-L5100DN'].obj.print_technology)

# Принтер Brother HL-L5100DN - 3ед. принято на склад Главный
# Принтер Brother HL-L5100DN - 2ед. принято на склад Главный
# Сканер HP ScanJet 7500 - 4ед. принято на склад Главный
# Принтер Brother HL-L5100DN - 2ед. отправлено в Бухгалтерия
# Принтер Brother HL-L5100DN - 2ед. отправлено в Отдел Кадров
# Сканер HP ScanJet 7500 - 2ед. отправлено в Отдел Кадров
# Содержимое склада Главный:
# --------
# Принтер Brother HL-L5100DN - 1ед.
# Сканер HP ScanJet 7500 - 2ед.
#
# Лазерный

# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
# булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат. Выполните вызов методов и также покажите результат.


class Car:

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self, speed):
        if speed >= 0:
            self.speed = speed
        print(str.format('{} поехала со скоростью {}км/ч', self.name, self.speed))

    def stop(self):
        self.speed = 0
        print(str.format('{} остановилась', self.name))

    def turn(self, direction):
        print(str.format('{} повернула {}', self.name, direction))

    def show_speed(self):
        print(str.format('{}км/ч', self.speed))


class TownCar(Car):

    def show_speed(self):
        print(str.format('{}км/ч', self.speed))
        if self.speed > 60:
            print("Превышение скорости!")


class SportCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.name = 'Cпортивная ' + name


class WorkCar(Car):

    def show_speed(self):
        print(str.format('{}км/ч', self.speed))
        if self.speed > 40:
            print("Превышение скорости!")


class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


police_car = PoliceCar(40, 'Черная', 'Volvo')
print(police_car.is_police)
sport_car = SportCar(90, 'Красная', 'Ferrari')
print(sport_car.name)
town_car = TownCar(25, 'Белый', 'Ford')
town_car.show_speed()
town_car.stop()
town_car.go(80)
town_car.show_speed()

# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
# порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод. Задачу
# можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
# завершать скрипт.

from time import sleep
from sys import exit


class TrafficLight:

    __lights = {
        'красный': ('желтый', 2),
        'желтый': ('зеленый', 5),
        'зеленый': ('красный', 7)
                }

    def __init__(self, color):
        color = str(color).lower()
        if color in TrafficLight.__lights.keys():
            self.__color = color
        else:
            raise ValueError

    def running(self, new_color):
        proper_light = TrafficLight.__lights[self.__color]
        if new_color != proper_light[0]:
            print('Нарушен порядок цветов!')
            exit()
        else:
            self.__color = new_color
            print(self.__color)
            for i in range(proper_light[1], 0, -1):
                print(i)
                sleep(1)


my_traffic_light = TrafficLight('Красный')
my_traffic_light.running('желтый')
my_traffic_light.running('зеленый')
my_traffic_light.running('красный')
my_traffic_light.running('зеленый')
my_traffic_light = TrafficLight('Синий')

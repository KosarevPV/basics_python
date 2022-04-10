class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        self.direction = direction
        print(f'{self.name} поехала {self.direction}')

    def show_speed(self):
        print(f'Текущая скорость {self.name} - {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed <= 60:
            print(f'Текущая скорость {self.name} - {self.speed}')
        else:
            print(f'Текущая скорость {self.name} - {self.speed}')
            print(f'У {self.name} превышении скорости')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed <= 40:
            print(f'Текущая скорость {self.name} - {self.speed}')
        else:
            print(f'Текущая скорость {self.name} - {self.speed}')
            print(f'У {self.name} превышении скорости')


class PoliceCar(Car):
    pass


t_car = TownCar(61, 'blue', 'town', False)
s_car = SportCar(120, 'black', 'sport', False)
w_car = WorkCar(30, 'red', 'work', False)
p_car = PoliceCar(60, 'white', 'police', True)

p_car.go()
s_car.stop()
w_car.turn('направо')
t_car.show_speed()
w_car.show_speed()

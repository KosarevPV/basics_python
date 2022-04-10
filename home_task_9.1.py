import time


class TrafficLight:
    __color = ['красный', 'жёлтый', 'зеленый']
    __running = [7, 2, 1]

    def change_color(self):
        while True:
            print(self.__color[0])
            time.sleep(self.__running[0])
            print(self.__color[1])
            time.sleep(self.__running[1])
            print(self.__color[2])
            time.sleep(self.__running[2])
            print(self.__color[1])
            time.sleep(self.__running[1])


t_l = TrafficLight()
t_l.change_color()

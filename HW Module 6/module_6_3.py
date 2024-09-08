class Horse:
    '''
    Класс описывающий лошадь
    '''

    def __init__(self, y_distance):
        self.x_distance = 0  # пройденный путь.
        self.sound = 'Frrr'  # звук, который издаёт лошадь.
        super().__init__(y_distance)
        super().fly()

    def run(self, dx):  # изменение дистанции на значение dx
        self.x_distance += dx


class Eagle:
    '''
    Класс описывающий орла
    '''

    def __init__(self):
        self.y_distance = 0  # пройденный путь.
        self.sound = 'I train, eat, sleep, and repeat'  # звук, который издаёт орёл.

    def fly(self, dy):  # изменение дистанции на значение dy
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    '''
    Класс описывающий пегаса
    '''

    def __init__(self, y_distance):
        super().__init__(y_distance)

    def move(self, dx, dy):  # изменение дистанции на значениe (dx, dy)
        super().fly(dy)  # Явно указываем, что хотим вызвать метод fly() класса Eagle
        super().run(dx)  # Явно указываем, что хотим вызвать метод run() класса Horse

    def get_pos(self):  # текущее положение пегаса
        position = (self.x_distance, self.y_distance)
        return position

    def voice(self):  # значение унаследованного атрибута sound
        print(f'{self.sound}')


# Код программы
p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()

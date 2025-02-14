class Vehicle:
    """ Базовый класс транспорт."""
    def __init__(self, name: str, speed: float):
        self._name = name
        self.speed = speed

    """В качестве атрибутов класс принимает наименование транспорта и его текущую скорость передвижения в км/ч"""

    def __str__(self) -> str:
        return f"Транспорт {self._name}. Скорость {self.speed} км/ч"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, speed={self.speed!r})"

    def trav_dist(self, hours: int) -> str:
        return f"Дистанция пройденная за {hours} часов равна {self.speed*hours}"

    """Метод рассчитывает и выводит сообщение о том, какую дистанцию может пройти транспорт за указанное кол-во часов"""

    @property
    def name(self) -> str:
        return self._name

    """Наименование транспорта укажем как неизменяемый атрибут"""
    """Атрибут speed оставим публичным, чтобы иметь возможность изменить текущую скорость движения транспортра"""


class Ship(Vehicle):
    """Дочерний класс морское судно"""
    def __init__(self, name: str, speed: float, load_capacity: int):
        super().__init__(name, speed)
        self.load_capacity = load_capacity

    """Помимо наследуемых атрибутов, добавим в конструктор атрибут 
    load_capacity отвечающий за грузоподъёмность морского судна"""

    def __str__(self) -> str:
        return f"Морское судно {self._name}. Скорость {self.speed} км/ч или {self.speed*0.54} уз. Грузоподъёмность " \
               f"{self.load_capacity}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, speed={self.speed!r}, " \
               f"load_capacity={self.load_capacity})"

    def trav_dist(self, hours: int) -> str:
        return f"Дистанция пройденная за {hours} часов равна {self.speed*hours} км или {self.speed*hours*0.54} узлов"

    """Методы __str__ и trav_dist перегружены, чтобы включать 
    в себя единицы измерения скорости для морских судов (узлы)"""


class Car(Vehicle):
    """Дочерний класс автомобиль"""
    def __init__(self, name: str, speed: float, fuel_capacity: int):
        super().__init__(name, speed)
        self.fuel_capacity = fuel_capacity

    """Помимо наследуемых атрибутов, добавим в конструктор атрибут 
    fuel_capacity отвечающий за вместимость топливного бака (в литрах)"""

    def __str__(self) -> str:
        return f"Морское судно {self.name}. Скорость {self.speed} км/ч. " \
               f"Вместимость топливного бака {self.fuel_capacity}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, speed={self.speed!r}, " \
               f"fuel_capacity={self.fuel_capacity})"

    def fuel_rate(self, distance) -> str:
        return f"Расход топлива автомобиля = {distance/self.fuel_capacity} л/км"

    """Добавим к существующему методу расчёта пройденного пути за время, метод, 
    рассчитывающий расход топлива автомобиля в зависимости от пройденного пути"""


if __name__ == "__main__":
    # Write your solution here
    pass

# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Reserve:
    def __init__(self, capacity: float = 1000, flow: float = 0, contains: float = 0) -> None:
        """
        Создание и подготовка к работе объекта "Резерв"
        :param capacity: Вместимость резерва
        :param flow: Поток материала из/в резерв
        :param contains: Текущее кол-во содержимого в резерве материала
    
        Примеры:
        >>> reserve = Reserve(500, 0, 250) # инициализация экземпляра класса
        """
        if not isinstance(capacity, (int, float)):
            raise TypeError("Вместимость резерва должна быть типа int или float")
        if capacity <= 0:
            raise ValueError("Вместимость резерва не может быть меньше 0")
        self.capacity = capacity

        if not isinstance(flow, (int, float)):
            raise TypeError("Поток материалов должен быть типа int или float")
        if flow > self.capacity:
            raise ValueError("Поток не может быть больше вместимости")
        self.flow = flow

        if not isinstance(contains, (int, float)):
            raise TypeError("Текущее кол-во материала в резерве должно быть типа int или float")
        if contains <= 0:
            raise ValueError("Текущее кол-во материала в резерве не может быть меньше 0")
        self.contains = contains

    def change_flow(self, new_flow) -> None:
        """
        Изменить поток материала в резерв
        :param new_flow: Новое значение потока материала
        :raise ValueError: Если абсолютное значение потока превысило вместимость резерва
        Примеры:
        >>> reserve = Reserve(500, 25, 225)
        >>> reserve.change_flow(-25)
        """
        if not isinstance(new_flow, (int, float)):
            raise TypeError("Новый поток материалов должен быть типа int или float")
        if new_flow > self.capacity:
            raise ValueError("Новый поток не может быть больше вместимости")

    def iterate(self) -> None:
        """
        Произвести одну итерацию потока материала
        :raise ValueError: Если текущее кол-во материала в резерве после итерации превысило вместимость ИЛИ текущее
        кол-во материала < текущего значения потока
        Примеры:
        >>> reserve = Reserve(500, 25, 225)
        >>> reserve.iterate()
        """

    def change_capacity(self, new_capacity) -> None:
        """
        Изменить вместимость резерва
        :param new_capacity: Новое значение вместимости резерва.
        :raise ValueError: Если новое значение вместимости меньше текущего значения потока
        Примеры:
        >>> reserve = Reserve(500, 25, 225)
        >>> reserve.change_capacity(750)
        """
        if not isinstance(new_capacity, (int, float)):
            raise TypeError("Новая вместимость резерва должна быть типа int или float")
        if new_capacity <= 0:
            raise ValueError("Новая вместимость резерва не может быть меньше 0")
        if new_capacity < self.flow:
            raise ValueError("Новая вместимость резерва не может быть меньше текущего потока")
        self.capacity = new_capacity


class Gears:
    def __init__(self, gear1: int = 1, gear2: int = 1) -> None:
        """
        Создание и подготовка к работе объекта "Шестерни"
        :param gear1: Число зубьев первой шестерни
        :param gear2: Число зубьев второй шестерни
        Примеры:
        >>> gears = Gears(6, 8)
        """

        if not isinstance(gear1, int):
            raise TypeError("Кол-во зубцов первой шестерни должно быть типа int")
        if gear1 <= 0:
            raise ValueError("Кол-во зубцов первой шестерни должно быть не меньше 0")
        self.gear1 = gear1

        if not isinstance(gear2, int):
            raise TypeError("Кол-во зубцов второй шестерни должно быть типа int")
        if gear2 <= 0:
            raise ValueError("Кол-во зубцов второй шестерни должно быть не меньше 0")
        self.gear2 = gear2

    def transfer_ratio(self) -> float:
        """
        Определение передаточного отношения зубчатой передачи
        :return: Число вещественного типа, отношение кол-ва зубцев первой шестерни ко второй
        Пример:
        >>> gears = Gears(10, 15)
        >>> gears.transfer_ratio()
        """

    def transfer_type(self) -> str:
        """
        Определение типа зубчатой передачи (Повышающая/Понижающая)
        :return: Строковое значение, выводящее тип передачи, в зависимости от отношения кол-ва зубцов шестерней
        Пример:
        >>> gears = Gears(20, 10)
        >>> gears.transfer_type()
        """


class TriangleAngles:
    def __init__(self, angle1: int = 60, angle2: int = 60, angle3: int = 60):
        """
        Создание и подготовка к работе объекта "Углы треугольника"
        :param angle1: Величина первого угла треугольника
        :param angle2: Величина второго угла треугольника
        :param angle3: Величина третьего угла треугольника
        Пример:
        >>> triangle = TriangleAngles(13, 95, 72)
        """
        if not isinstance(angle1, (int, float)):
            raise TypeError("Первый угол треугольника должен быть типа int или float")
        if angle1 <= 0:
            raise ValueError("Первый угол треугольника не может быть отрицательным")
        self.Angle1 = angle1

        if not isinstance(angle2, (int, float)):
            raise TypeError("Второй угол треугольника должен быть типа int или float")
        if angle2 <= 0:
            raise ValueError("Второй угол не может быть отрицательным")
        self.angle2 = angle2

        if not isinstance(angle3, (int, float)):
            raise TypeError("Третий угол должен быть типа int или float")
        if angle3 <= 0:
            raise ValueError("Третий угол не может быть отрицательным")
        self.angle3 = angle3

        if (angle1 + angle2 + angle3) != 180:
            raise ValueError("Сумма углов треугольника не может быть меньше или больше 180 градусов")

    def isIsosceles(self) -> bool:
        """
        Проверка треугольника на равнобедренность
        :return: Логическое значение. True/False в зависимости от того являются ли как минимум два угла треугольника
        равными или нет
        Пример:
        >>> triangle = TriangleAngles(75, 75, 30)
        >>> triangle.isIsosceles()
        """

    def isRectangular(self) -> bool:
        """
        Проверка треугольника на прямоугольность
        :return: Логическое значение. True/False в зависимости от того является ли один из углов треугольника
        прямым или нет
        Пример:
        >>> triangle = TriangleAngles(90, 60, 30)
        >>> triangle.isRectangular()
        """

    def isEquiliteral(self):
        """
        Проверка треугольника на равносторонность
        :return: Логическое значение. True/False в зависимости от того являются ли все три угла треугольника
        равными собой или нет
        Пример:
        >>> triangle = TriangleAngles(60, 60, 60)
        >>> triangle.isEquiliteral()
        """


if __name__ == "__main__":
    doctest.testmod()

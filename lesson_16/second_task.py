from abc import ABC, abstractmethod
class Figure:
    @abstractmethod
    def get_area(self):
        pass
    @abstractmethod
    def get_perimeter(self):
        pass


class Square(Figure):
    def __init__(self, side):
        self.__side = side

    def get_area(self):
        return self.__side ** 2

    def get_perimeter(self):
        return self.__side * 4



class Rectangle(Figure):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height


    def get_area(self):
        return self.__width * self.__height

    def get_perimeter(self):
        return 2 * (self.__width + self.__height)


class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def get_area(self):
        return 3.14 * self.__radius ** 2

    def get_perimeter(self):
        return 2 * 3.14 * self.__radius



square = Square(12)
rectangle = Rectangle(7, 4)
circle = Circle(8)

figures = [square, rectangle, circle]


for i, figure in enumerate(figures, 1):
    print(f"Фігура {i}: {figure.__class__.__name__}")
    print(f"  Площа: {figure.get_area()}")
    print(f"  Периметр: {figure.get_perimeter()}")


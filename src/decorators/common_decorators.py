import atexit
from abc import abstractmethod


class Shape:
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    my_side = 0
    inner_type = "square"

    @classmethod
    def get_type(cls):
        return cls.inner_type

    @property
    def side(self):
        print("Getting side")
        return self.my_side

    @side.setter
    def side(self, value):
        print("Setting side")
        self.my_side = value

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return self.side * 4


@atexit.register
def clean_up():
    print("Cleaning up!")


if __name__ == "__main__":
    square = Square()
    square.side = 10
    print(square.side)
    print(square.area())
    print(square.perimeter())
    print(square.get_type())

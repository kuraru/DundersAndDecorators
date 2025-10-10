"""Minimal example for dunders."""

class MyObject:
    def __init__(self, value):
        self.value = value

    def __add__(self, right_obj):
        return MyObject(self.value + right_obj.value)

if __name__ == '__main__':
    left_obj = MyObject(1)
    print(left_obj)
    right_obj = MyObject(2)
    print(left_obj)
    print(right_obj)
    print(left_obj + right_obj)

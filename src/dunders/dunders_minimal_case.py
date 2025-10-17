"""Minimal example for dunders."""

class MyObject:
    def __init__(self, value: int):
        self.value = value

    def __add__(self, right_obj: "MyObject") -> "MyObject":
        return MyObject(self.value + right_obj.value)

    def __str__(self) -> str:
        return str(self.value)

if __name__ == '__main__':
    left_obj = MyObject(1)
    right_obj = MyObject(2)

    print(left_obj)
    print(right_obj)

    concatenated = str(left_obj) + str(right_obj)
    print(f"{left_obj} + {right_obj} = {concatenated}")

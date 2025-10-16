"""Minimal example for dunders."""


class MyObject:
    def __init__(self, value):
        # Garantiza que el valor sea convertible a entero
        self.value = int(value)

    def __add__(self, right_obj):
        # Concatenar como strings y convertir a entero
        concatenated = int(str(self.value) + str(right_obj.value))
        return MyObject(concatenated)

    def __repr__(self) -> str:
        # Devuelve representación como entero en forma de string, solo para ser impreso
        return str(self.value)


if __name__ == "__main__":
    left_obj = MyObject(1)
    print(left_obj)  # Output: 1
    right_obj = MyObject(2)
    print(right_obj)  # Output: 2
    print(left_obj + right_obj)  # Output: 12

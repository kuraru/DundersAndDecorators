"""Dunders basic example."""

class MyString:
    """MyString class definition."""
    def __init__(self, string):
        # store as bytes to keep original style
        self.string = string.encode('utf-8')

    def _text(self) -> str:
        return self.string.decode('utf-8')

    def copy(self):
        """Make a shallow copy."""
        return MyString(self._text())

    def __str__(self):
        """String representation (original text)."""
        return self._text()

    def __add__(self, other):
        """Concatenate two MyString objects."""
        return MyString(self._text() + other._text())

    def __sub__(self, other):
        """Remove the first occurrence of other's text from self."""
        left_op = self._text()
        right_op = other._text()
        if right_op in left_op:
            return MyString(left_op.replace(right_op, '', 1))
        return self.copy()

    def __mul__(self, times):
        """Repeat the string times times (MyString * int)."""
        if isinstance(times, int):
            if times < 0:
                raise ValueError("Repetition times must be >= 0")
            return MyString(self._text() * times)
        raise TypeError("Can only multiply MyString by int")

    def __truediv__(self, other):
        """
        Real division based on character length.
        - MyString / MyString -> float (len_chars(self) / len_chars(other))
        - MyString / (int|float) -> float (len_chars(self) / number)
        """
        left_len = len(self._text())
        if isinstance(other, MyString):
            right_len = len(other._text())
            return left_len / right_len
        if isinstance(other, (int, float)):
            return left_len / other
        raise TypeError("Division supports MyString or number as the divisor")

    def __len__(self):
        """
        Word count:
        - len(MyString('')) == 0
        - len(MyString('hello there')) == 2
        """
        text = self._text().strip()
        if not text:
            return 0
        return len(text.split())


if __name__ == '__main__':
    a = MyString('hello')
    b = MyString('there')

    print(a)
    print(a + b)
    print((a + b) - b)
    print(a.copy() is a)

    print(a * 3)                  

    print(a / b)
    print(a / 2)

    print(len(MyString('')))
    print(len(MyString('hello there')))

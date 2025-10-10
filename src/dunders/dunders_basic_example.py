"""Dunders basic example."""

class MyString:
    """MyString class definition."""
    def __init__(self, string):
        self.string = string.encode('utf-8')

    def __str__(self):
        """string representation."""
        return self.string.decode('utf-8')

    def __add__(self, other):
        """Adding two strings."""
        return MyString(self.string.decode('utf-8') + other.string.decode('utf-8'))

    def __sub__(self, other):
        """Subtracting two strings."""
        left_op = self.string.decode('utf-8')
        right_op = other.string.decode('utf-8')
        if right_op in left_op:
            return MyString(left_op.replace(right_op, '', 1))
        return self.copy()

    def copy(self):
        """make a shallow copy."""
        return MyString(self.string.decode('utf-8'))


if __name__ == '__main__':
    my_string = MyString('hello')
    print(my_string)
    my_new_string = my_string + my_string
    print(my_new_string)
    print(my_new_string - my_string)
    my_last_string = my_string.copy()
    print(my_string is my_last_string)


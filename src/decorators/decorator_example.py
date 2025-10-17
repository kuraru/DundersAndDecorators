def my_decorator_n(n: int):
    """A decorator that prints messages before and after a function n times."""
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be >= 0")

    def decorator(f):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                print("Before function")
            result = f(*args, **kwargs)
            for _ in range(n):
                print("After function")
            return result
        return wrapper
    return decorator


@my_decorator_n(2)
def execute_task(t):
    print(f"executing task: {t}")


if __name__ == "__main__":
    execute_task("Sample Task")

def my_decorator(f):
    def wrapper():
        print("Before function")
        f()
        print("After function")
    return wrapper


@my_decorator
def execute_task():
    print("Executing task…")


def do_twice(f):
    def wrapper_do_twice(*args, **kwargs):
        f(*args, **kwargs)
        f(*args, **kwargs)
    return wrapper_do_twice


@do_twice
def count_to(n):
    message = "".join([i for i in range(1, n+1)])


if __name__ == "__main__":
    execute_task()
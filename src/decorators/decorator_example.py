def my_decorator(f):
    def wrapper(n):
        print("Before function")
        f(n)
        print("After function")
    return wrapper

# @my_decorator
# def execute_task():
#     print("Executing task…")


def do_twice(f):
    def wrapper_do_twice(*args, **kwargs):
        f(*args, **kwargs)
        f(*args, **kwargs)
    return wrapper_do_twice


# @do_twice
# def count_to(n):
#     message = "".join([str(i) for i in range(1, n+1)])
#     print(message)

def do_n_times(n):
    def decorator(f):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                f(*args, **kwargs)

        return wrapper

    return decorator

@do_n_times(3)
def count_to(n):
    message = "".join([str(i) for i in range(1, n + 1)])
    print(message)


def my_decorator_n(n): #Acepta un argumentos
    def decorator(f):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                print("Before function")
            f(*args, **kwargs)
            for _ in range(n):
                print("After function")

        return wrapper

    return decorator


@my_decorator_n(5)
def execute_task(t):
    print(f"executing task: {t}")


if __name__ == "__main__":
    execute_task(10)
    count_to(7)

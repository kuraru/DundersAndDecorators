def outer_func():
    value = 1
    def inner_func():
        print(f"{value}")
    return inner_func


def outer_func_2():
    value = 1
    return lambda: print(f"{value}")


def outer_func_3():
    value = 1
    def inner_func():
        nonlocal value
        value += 1
        print(f"{value}")
    return inner_func


def outer_func_4():
    arr_values = []
    def inner_func():
        arr_values.append(1)
        print(f"{arr_values}")
    return inner_func

if __name__ == "__main__":
    inner_func = outer_func()
    inner_func()
    inner_func = outer_func_2()
    inner_func()
    inner_func = outer_func_3()
    inner_func()
    inner_func = outer_func_4()
    inner_func()

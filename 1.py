
def task_1(a, b, c) -> tuple:
    a, b, c = b, c, a
    return (a, b, c)


print(task_1(1, 2, 3))


def task_2(a, b):
    if isinstance(a, (int, float)) or isinstance(b, (int, float)):
        return a+b
    else:
        raise TypeError


def task_1(a, b, c) -> tuple:
    a, b, c = b, c, a
    return (a, b, c)


# print(task_1(1, 2, 3))


def task_2():
    while True:
        a, b = input().split()
        try:
            a = float(a)
            b = float(b)
        except ValueError:
            continue
        else:
            break

    return a+b


# print(task_2(1.2, 2))
def task_2_2():
    numbers = []
    N = int(input("Введите колво чисел"))
    while N > 0:
        a = input()

        try:
            a = float(a)
            numbers.append(a)
        except ValueError:
            N += 1

        else:
            N -= 1
    print(sum(numbers))
    return sum(numbers)


task_2_2()

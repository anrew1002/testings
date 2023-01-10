import datetime
import math
import time
from random import randint

from memory_profiler import profile


@profile
def task_1() -> tuple:
    start = datetime.datetime.now()
    a, b, c = input("три значения через пробел: ").split()
    a, b, c = b, c, a
    end = datetime.datetime.now()
    print(f"Время затраченное на task_1 {end-start}")
    print(a, b, c)


print("TASK_1")
task_1()


def task_2():
    while True:
        a, b = input("Введите два числа: ").split()
        try:
            a = float(a)
            b = float(b)
        except ValueError:
            print("Ошибка")
            continue
        else:
            break

    print(a+b)


print("TASK_2")
task_2()


def task_2_2():
    numbers = []
    N = int(input("Введите колво чисел"))
    while N > 0:
        a = input()
        try:
            a = float(a)
            numbers.append(a)
        except ValueError:
            continue
        else:
            N -= 1
    print("сумма= ", sum(numbers))
    return sum(numbers)


print("TASK_2_2")
task_2_2()


@profile
def task_3_1(x):
    start = datetime.datetime.now()
    print(x**5)
    end = datetime.datetime.now()
    print(f"Затраченное время: {end-start}")


print("TASK_3_1 c значением 5:")
task_3_1(5)
print()


@profile
def task_3_2(x):
    start = datetime.datetime.now()
    out = 1
    for i in range(5):
        out *= x
    end = datetime.datetime.now()
    print(f"Затраченное время: {end-start}")
    return out


print("TASK_3_2 c значением 5:")
print(task_3_2(5))
print()


def task_4(x: int) -> bool:
    i = 0
    a = 1
    fibonachi = []
    while i <= 250:
        i += a
        a = i - a
        fibonachi.append(i)
    if x <= 250:
        if x in fibonachi:
            return True
        return False


print("TASK_4:")
x = int(input("введите число: "))
print(task_4(x))
print()


def task_5(month: int):
    dict_moth = {'Зима': (1, 2, 12),
                 'Весна': (3, 4, 5),
                 'Лето': (6, 7, 8),
                 'Осень': (9, 10, 11)}
    print([key for key in dict_moth.keys() if month in dict_moth[key]])

    num = month
    if (num <= 2) or (num == 12):
        return "Зима"
    if (num >= 3) and (num <= 5):
        return "Весна"
    if (num >= 6) and (num <= 8):
        return "Лето"
    if (num >= 9) and (num <= 11):
        return "Осень"


print("TASK_5:")
x = int(input("введите число: "))
task_5(x)
print()


def task_6(N):

    sum = 0
    even = 0
    not_even = 0
    for i in range(N):
        sum += i
        if i % 2 == 0:
            even += 1
        else:
            not_even += 1
    return sum, even, not_even


print("TASK_6:")
x = int(input("введите число: "))
print(task_6(x))
print()


@profile
def task_7(N):
    def del_search(num):
        delit = 1
        output = set()
        # проходит только до корня, записывает парный делитель
        while delit <= num**0.5:
            if num % delit == 0:
                output.add(delit)
                output.add(num//delit)
            delit += 1
        return output
    start = datetime.datetime.now()
    for i in range(1, N+1):
        print(i, del_search(i))
    end = datetime.datetime.now()
    print(f"Затраченное время: {end-start}")


print("TASK_7:")
x = int(input("введите число: "))
task_7(x)
print()


@profile
def task_8():
    N, M = map(int, input("Введите N и M: ").split())
    for b in range(N, M):
        for a in range(N, b):
            c = math.sqrt(a * a + b * b)
            if c % 1 == 0:
                return a, b, int(c)


print("TASK_8:")
print(task_8())
print()


def task_9(N, M):
    def is_del(num):
        for i in str(num):
            if int(i) == 0 or num % int(i) != 0:
                return False
        return True

    for i in range(N, M+1):
        if is_del(i):
            print(i)


print("TASK_9:")
N = int(input("Введите N: "))
M = int(input("Введите M: "))
task_9(N, M)
print()


def task_10(N):
    def del_search(a):
        if a == 1:
            return 1
        sum_num = 0
        for i in range(1, a // 2 + 1):
            if a % i == 0:
                sum_num += i
        return sum_num

    N, i = 1, 1
    f = []
    while N < 5:
        i += 1
        if i == del_search(i):
            f.append(i)
            N += 1
    return f


print("TASK_10: для 4 чисел")
print(task_10(4))
print()


def task_11():
    mac = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    start1 = time.time()
    print(mac[-1])
    end1 = time.time()

    start2 = time.time()
    print(next(reversed(mac)))
    end2 = time.time()

    start3 = time.time()
    print(mac.pop())
    end3 = time.time()

    print(
        f"срез: {start1 - end3}, reversed: {start2 - end2}, pop: {start3 - end3}")


print("TASK_11")
task_11()
print()


def task_12():
    mac = [1, 2, 3, 4, 5]
    return mac[::-1]


print("TASK_12")
print(task_12())
print()


def task_13():
    def sum_list(l, res, i=0):
        if i == len(l):
            return res
        else:
            res += l[i]
            i += 1
            return sum_list(l, res, i)

    list_num = [1, 2, 3, 4, 5]
    print(sum_list(list_num, 0))


print("TASK_13")
task_13()
print()

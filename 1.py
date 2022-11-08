
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


def task_3_1(x):
    return x**5


def task_3_2(x):
    out = 1
    for i in range(5):
        out *= x
    return out


# x = 2
# print(task_3_2(x))

# print(task_3_1(x))

def task_4(x: int) -> bool:
    if x <= 250:
        fibonachi = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
        if x in fibonachi:
            return True
        return False


def task_5(month: int):
    num = month
    if num <= 2:
        return "winter"
    if num <= 5:
        return "spring"
    if num <= 8:
        return "summer"
    if num <= 11:
        return "autumn"


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


def task_7(N):
    def del_search(num):
        delit = 1
        output = set()
        while delit <= num**0.5:
            if num % delit == 0:
                output.add(delit)
                output.add(num//delit)
            delit += 1
        return output
    for i in range(1, N+1):
        print(i, del_search(i))


def task_9(N, M):
    def is_del(num):
        for i in str(num):
            if int(i) == 0 or num % int(i) != 0:
                return False
        return True

    for i in range(N, M+1):
        if is_del(i):
            print(i)


# task_9(10, 25)


def task_10(N):
    def del_search(num):
        delit = 1
        output = set()
        while delit <= num**0.5:
            if num % delit == 0:
                output.add(delit)
                output.add(num//delit)
            delit += 1
        return output

    num = 1
    output = []
    while len(output) < N:
        flag = True
        for deli in del_search(num):
            print(del_search(num))
            print("1", deli)
            if num % deli != 0:
                flag = False
                break
        if flag:
            print(num)
            output.append(num)
        num += 1
    return output


print(task_10(3))

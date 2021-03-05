from common import timer


def my_abs(x):  # 计算绝对值
    if x >= 0:
        return x
    else:
        return -x


def nop():  # 什么也不做
    pass  # 什么也不做,类似continue


def power(x, n=2):  # 计算自己乘积 默认参数
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


def fact(n):  # 计算阶乘  递归 会导致栈溢出
    if n == 1:
        return 1
    return n * fact(n - 1)


def fact2(n):  # 计算阶乘 尾递归 循环是一种特殊的尾递归
    return fact2_iter(n, 1)


def fact2_iter(num, product):
    if num == 1:
        return product
    return fact2_iter(num - 1, num * product)


def get_square1(x, n=1):  # 计算自己乘积 普通list
    result = list()
    for i in range(x):
        result.append(pow(i, n))
    return result


def get_square2(x, n=1):  # 计算自己乘积  yield构造生成器 节省内存
    for i in range(x):
        yield(pow(i, n))


@timer
def square1(x, n=1):  # 遍历list 效率低
    a = get_square1(x, n)
    for i in a:
        print(i, end=', ')
    # print(get_square1(x, n))


@timer
def square2(x, n=1):  # 遍历iter 效率高
    a = get_square2(x, n)
    a_iter = iter(a)  # 迭代函数 iter，用于生成迭代器
    for i in a_iter:
        print(i, end=', ')


class Myclass:
    x = 1

    @staticmethod
    def factStatic(n):  # 计算阶乘  递归 会导致栈溢出
        if n == 1:
            return 1
        return n * fact(n - 1)

    def factNotStatic(self, n):  # 计算阶乘  递归 会导致栈溢出
        self.x = 2
        print(self.x)
        if n == 1:
            return 1
        return n * fact(n - 1)

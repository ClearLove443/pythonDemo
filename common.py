import time


def timer(func):  # 计算方法运行时间 timer() 是我们定义的装饰器函数
    def wrapper(*args, **kwds):  # 一颗星表示不限数量的单值参数，两颗星表示不限数量的键值对参数。
        t0 = time.time()
        func(*args, **kwds)
        t1 = time.time()
        print('耗时%0.3f' % (t1-t0,), 's')
    return wrapper

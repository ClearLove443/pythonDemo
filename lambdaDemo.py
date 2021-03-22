# f = lambda x: x * x
f = lambda x, y = 1: f(x - 1, x + y) if x > 1 else y  # 尾递归
print(f(999))

f2 = lambda x: x + f2(x - 1) if x > 1 else 1  # 递归
# print(f2(1000))

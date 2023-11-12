# counter = 100  # 赋值整型变量
# miles = 1000.0  # 浮点型
# name = "John"  # 字符串

# print(counter)
# print(miles)
# print(name)
# print(counter, miles)

# # name = input()
# # print('name:', name)

# print(True or False)
# print(True and False)
# print(ord('中'))
# print(chr(ord('中')))

# print(1+3+4)

# sum = 0
# for x in range(101):
#     sum = sum + x
# print(sum)

# d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# d['Michael'] = 100

# # if作用域是通过缩进控制的
# if 'Michael2' in d:
#     print(d['Michael'])

# print(d['Michael'])

import json
import os

from abstest import (
    Myclass,
    fact,
    fact2,
    fact2_iter,
    get_square2,
    my_abs,
    power,
    square1,
    square2,
)

# a = abs
# print(a(-22))

# print(max(-22, 22, 55))

# print(my_abs(-33))

# print(power(-33))
# print(power(2, 3))
# print(fact(10))

# print(fact(1000)) #栈溢出
# print(fact2(1000))  # 尾递归 由于编辑器没有对尾递归进行优化.还是会造成栈溢出

# a = get_square(1000100)
# a_iter = iter(a)  # 迭代函数 iter，用于生成迭代器


# square1(1000100)  # 遍历list 效率低
# square2(1000100)  # 遍历iter 效率高


# with as 适合一些事先需要准备，事后需要处理的任务
# fp = open(r"abstest.py", 'r')
# try:
#     contents = fp.readlines()
# finally:
#     fp.close()

# 读取文件
file_path = "abstest.py"
with open(file_path, "r", encoding="utf-8") as fp:
    contents = fp.readlines()
print(type(contents))
contents2 = "".join(contents)
# print(contents)

# 删除文件
# if os.path.exists("abstestbak.py"):
#     os.remove("abstestbak.py")

# 创建新文件
# 如需在 Python 中创建新文件，请使用 open() 方法，并使用以下参数之一：

# "x" - 创建 - 将创建一个文件，如果文件存在则返回错误
# "a" - 追加 - 如果指定的文件不存在，将创建一个文件
# "w" - 写入 - 如果指定的文件不存在，将创建一个文件，会覆盖原文件
file_path = "abstestbak.py"
with open(file_path, "a", encoding="utf-8") as fp2:
    # fp2.write("".join(contents))
    fp2.writelines(contents)


# p1 = Myclass() # 创建新对象
# print(p1.x)
# print(p1.factStatic(5))  # 调用静态方法
# print(Myclass.factStatic(5))  # 调用静态方法
# print(p1.factNotStatic(6))  # 调用非静态方法


# # 一些 JSON:
# x = '{ "name":"Bill", "age":63, "city":"Seatle"}'

# # 解析 x:
# y = json.loads(x)

# # 结果是 Python 字典：
# for i in y:
#     print(i)
#     print(y[i])

# 遍历 list
# for i in sql:  有 bug list多个值相同的时候，取的下标不正确
#     try:
#         await conn.fetch(i)
#         hasChannel.append(sql.index(i) + 1)
#     except Exception:
#         noChannel.append(sql.index(i) + 1)

# for i in range(len(sql)):
#     try:
#         await conn.fetch(sql[i])
#         hasChannel.append(i + 1)
#     except Exception:
#         noChannel.append(i + 1)

# 遍历 map
# for key in sql:
#     try:
#         await conn.fetch(sql[key])
#         hasChannel.append(key)
#     except Exception:
#         noChannel.append(key)
# print('hasChannelCode', hasChannel)
# print('noChannelCode', noChannel)

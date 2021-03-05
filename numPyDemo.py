import matplotlib.pyplot as plt
import numpy as np  # 别名导入

# arr = np.array([1, 2, 3, 4, 5])

# print(arr)
# print(type(arr))


# arr = np.array([1, 2, 3, 4], ndmin=5)  # 多维数组

# print(arr)
# print('number of dimensions :', arr.ndim)


# x = numpy.random.uniform(0.0, 5.0, 250)

# plt.hist(x, 5)
# plt.show()

x = np.random.normal(5.0, 1.0, 100000)

plt.hist(x, 100)
plt.show()

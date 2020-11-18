import numpy as np

nested_list = [[1, 2], [3, 4]]
print(nested_list)
# 输出：[[1, 2], [3, 4]]

# 二维数组
data = np.array(nested_list)
print(data)
# 输出：
# [[1 2]
#  [3 4]]

ones = np.ones((3, 2))
print(ones)
# 输出：
# [[1. 1.]
#  [1. 1.]
#  [1. 1.]]

zeros = np.zeros((3, 2))
print(zeros)
# 输出：
# [[0. 0.]
#  [0. 0.]
#  [0. 0

data = np.array([[1, 2], [3, 4], [5, 6]])

print(data[0, 1])
# 输出：2

print(data[:, 0])
# 输出：[1 3 5]

print(data[1:3])
# 输出：
# [[3 4]
#  [5 6]]

ones = np.ones((2, 3))
data = np.array([1, 2, 1])
print(ones + data)


import numpy as np

data = np.genfromtxt('data.csv', delimiter=',')

print(data)

predictions = np.array([1, 1, 1])
labels = np.array([1, 2, 3])
error = (1 / labels.size) * np.sum(np.square(predictions - labels))
print(error)
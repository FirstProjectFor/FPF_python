import numpy as np

print('一维数组  np.array([1, 2, 3]:\n {}'.format(np.array([1, 2, 3])))
print()
# 如果数组元素个数不一致，会生成一维数组，数组的元素是 list
print('二维数组  np.array([[1, 2, 3], [2, 3, 4]])):\n {}'.format(np.array([[1, 2, 3], [2, 3, 4]])))
print()
print('指定最小维度  np.array([[3, 4, 3]], ndmin=2):\n {}'.format(np.array([[3, 4, 3]], ndmin=2)))
print()
print('对角矩阵  np.eye(3):\n {}'.format(np.eye(3)))
print()
print('向量  np.array([1,  2,  3], dtype = complex):  \n{}'.format(np.array([1, 2, 3], dtype=complex)))

print(type(np.NAN))
print(type(np.NAN))
print(type(np.NAN))
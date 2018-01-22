# -*- coding: utf-8 -*-

import numpy as np

# 创建数组
a = np.array([0, 1, 2, 3, 4, 5])

# 打印数组内容
print("a = np.array([0, 1, 2, 3, 4, 5]) -> a = ", a)
# 打印数组形状：(6,) = 一维数组，有6个元素
print("a.shape = ", a.shape)

# 将数组转换为二维数组，形状为(3行,2列)
b = a.reshape((3, 2))
print("b = a.reshape((3, 2)) -> b = \n", b)

# 打印b数组的形状
print("b.shape = ", b.shape)

# 打印b数组一共有几维
print("b.ndim = ", b.ndim)

# 修改数组b的元素[1][0]为77
b[1][0] = 77
print("b[1][0] = 77 -> b = \n", b)
# 修改b数组的元素时，a数组也同时发生变化，说明b数组的元素是对a数组的引用
print("b[1][0] = 77 -> a = ", a)

# 当需要一个a转型后的副本时，需要转型完成后进行拷贝
c = a.reshape((3, 2)).copy()
print("a.reshape((3, 2)).copy() -> c = \n", c)
c[1][0] = 88
print("c[1][0] = 88 -> c = \n", c)
print("c[1][0] = 88 -> a = ", a)

a = np.array([1, 2, 3, 4, 5])
print("a = np.array([1,2,3,4,5])")
print("a * 2 = ", a * 2)
print("a ** 2 = ", a ** 2)

# python list 的 * 2 和numpy的结果不一样，list的*2是复制一份元素
list = [1, 2, 3, 4, 5]
print("list = ", list)
print("list * 2 = ", list * 2)

# 通过索引获取数组内的元素
a = np.array([1, 2, 3, 4, 5, 6])
print("a = ", a)
print("a[np.array([2, 3, 4])] = ", a[np.array([2, 3, 4])])

# 将二维数组转换为1维数组
print("b = \n", b)
print("b.reshape((6,)) = ", b.reshape((6,)))
print("len(b) = ", len(b))

# 通过对数组使用过滤条件以筛选元素
a = np.array([1, 2, 3, 4, 5, 6])
print("a = ", a)
print("a > 4 = ", a > 4)
# 将元素控制在某个区间,超过范围的数值将用边界值填充
print("a[a > 4] = ", a[a > 4])
print("a.clip(0,4) = ", a.clip(0, 4))
print("a.clip(2,3) = ", a.clip(2, 4))

# 用NAN标识不存在的数值
c = np.array([1, 2, 3, np.NAN, 5, 6])
print("c = ", c)
print("np.isnan(c) = ", np.isnan(c))
# 有NAN的值，求平均则为NAN
print("np.mean = ", np.mean(c))
#  c[~np.isnan(c)] 筛选c数组中，不是NAN的数据组成新的数组
print("c[~np.isnan(c)] = ", c[~np.isnan(c)])
print("np.mean(c[~np.isnan(c)]) = ", np.mean(c[~np.isnan(c)]))

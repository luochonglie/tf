#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/01/23 11:10
# @Author  : c0l0121
# @File    : web_traffic_all_data.py
# @Desc    :

import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import math


def error(f, x, y):
    """残差函数

    :param f: 函数
    :param x: 自变量集合
    :param y: 因变量集合
    :return: 残差
    """
    return sp.sum((f(x) - y) ** 2)


# 读入数据
data = np.genfromtxt('../dataset/mlsd/ch01/web_traffic.tsv', delimiter='\t')
print("data[:10] = ", data[:5])
print("data.shape = ", data.shape)

# 将数据拆分成x和y两组向量
x = data[:, 0]
y = data[:, 1]

# 查看有多少个y值是NAN
print("np.sum(np.isnan(y)) = ", np.sum(np.isnan(y)))

x = x[~np.isnan(y)]
y = y[~np.isnan(y)]

print("len(x) = ", len(x))

# 使用scipy的polyfit函数找到最小化误差的函数
# sp.polyfit(x, y, deg=1, full=True)
# deg : 阶数，1=一阶函数
# full : 输出更详尽的信息
fp1, residuals, rank, sv, rcond = sp.polyfit(x, y, deg=1, full=True)

# fp1 函数的参数，数组形式[2.59619213, 989.02487106] -> y = 2.59619213 * x + 989.02487106
print("Model parameters : %s" % fp1)

# 误差
print("Residuals : ", residuals)

# 输入参数fp1，用scipy生成函数
f1 = sp.poly1d(fp1)
print("error(f1,x,y) =  ", error(f1, x, y))

# 生成2阶函数
fp2 = sp.polyfit(x, y, 2)
f2 = sp.poly1d(fp2)
print("error(f2,x,y) =  ", error(f2, x, y))

fp3 = sp.polyfit(x, y, 3)
f3 = sp.poly1d(fp3)
print("error(f3,x,y) =  ", error(f3, x, y))

fp10 = sp.polyfit(x, y, 10)
f10 = sp.poly1d(fp10)
print("error(f10,x,y) = ", error(f10, x, y))

fp50 = sp.polyfit(x, y, 50)
f50 = sp.poly1d(fp50)
print("error(f50,x,y) = ", error(f50, x, y))

# 用散点图输出数据点
plt.scatter(x, y, s=2, alpha=0.8)

# 输出1阶函数
fx = sp.linspace(x[0], x[-1], 1000)  # 生成画图用的x
plt.plot(fx, f1(fx), color="g", label="d=%i" % f1.order)

# 输出2阶函数
plt.plot(fx, f2(fx), color="c", label="d=%i" % f2.order)

plt.plot(fx, f3(fx), color="m", label="d=%i" % f3.order)
plt.plot(fx, f10(fx), color="y", label="d=%i" % f10.order)
plt.plot(fx, f50(fx), color="r", label="d=%i" % f50.order)

plt.title("Web traffic over last month")
plt.xlabel("Time")
plt.ylabel("Hits/Hour")
plt.xticks([w * 7 * 24 for w in range(10)], ['week %i' % w for w in range(10)])
plt.autoscale(tight=True)
plt.grid()
plt.legend()
plt.show()

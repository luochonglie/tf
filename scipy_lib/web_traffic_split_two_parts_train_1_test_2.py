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
from scipy.optimize import fsolve


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

# 3.5有个拐点，因此将数据拆分成两段，分别求函数
inflection = math.ceil(3.5 * 7 * 24)
xa = x[:inflection]
ya = y[:inflection]
xb = x[inflection:]
yb = y[inflection:]

fa1 = sp.poly1d(sp.polyfit(xa, ya, 1))
fa2 = sp.poly1d(sp.polyfit(xa, ya, 2))
fa3 = sp.poly1d(sp.polyfit(xa, ya, 3))
fa10 = sp.poly1d(sp.polyfit(xa, ya, 10))
fa50 = sp.poly1d(sp.polyfit(xa, ya, 50))

print("error(fa1,  xb, yb) = %d" % error(fa1, xb, yb))
print("error(fa2,  xb, yb) = %d" % error(fa2, xb, yb))
print("error(fa3,  xb, yb) = %d" % error(fa3, xb, yb))
print("error(fa10, xb, yb) = %d" % error(fa10, xb, yb))
print("error(fa50, xb, yb) = %d" % error(fa50, xb, yb))

# 计算多少周的时候回达到每小时点击了10w
reached_max = fsolve(fa3 - 100000, 800) / (7 * 24)
print("100,000 hits/hour expected at week %f" % reached_max[0])

# 用散点图输出数据点
plt.scatter(x, y, s=2, alpha=0.8)

# 输出分段函数
fax = sp.linspace(xa[0], xa[-1], 800)
fbx = sp.linspace(xb[0], xb[-1], 200)
plt.plot(fax, fa1(fax), color="g", label="fa=%i" % fa1.order)
plt.plot(fbx, fa1(fbx), color="g", label="fa=%i" % fa1.order)

plt.plot(fax, fa2(fax), color="c", label="fa=%i" % fa2.order)
plt.plot(fbx, fa2(fbx), color="c", label="fa=%i" % fa2.order)

plt.plot(fax, fa3(fax), color="m", label="fa=%i" % fa3.order)
plt.plot(fbx, fa3(fbx), color="m", label="fa=%i" % fa3.order)

# 误差太大，不以图片输出
# plt.plot(fax, fa10(fax), color="y", label="fa=%i" % fa10.order)
# plt.plot(fbx, fa10(fbx), color="y", label="fa=%i" % fa10.order)
#
# plt.plot(fax, fa50(fax), color="r", label="fa=%i" % fa50.order)
# plt.plot(fbx, fa50(fbx), color="r", label="fa=%i" % fa50.order)

plt.title("Web traffic over last month")
plt.xlabel("Time")
plt.ylabel("Hits/Hour")
plt.xticks([w * 7 * 24 for w in range(10)], ['week %i' % w for w in range(10)])
plt.autoscale(tight=True)
plt.grid()
plt.legend()
plt.show()

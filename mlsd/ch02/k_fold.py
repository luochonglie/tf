#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/02/09 15:35
# @Author  : c0l0121
# @File    : k_fold.py
# @Desc    :


from sklearn.model_selection import KFold
import numpy as np

data = np.linspace(0, 100, 100)
label = np.array([1, 2, 3, 4])
# 5折交叉验证，80%为训练数据，20%为测试数据
kf = KFold(n_splits=5)

for train_idx, test_idx in kf.split(data):
    print("Train:", train_idx, "\nTest:", test_idx)

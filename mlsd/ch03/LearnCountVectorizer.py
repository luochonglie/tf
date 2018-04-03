#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/04/03 14:23
# @Author  : c0l0121
# @File    : LearnCountVectorizer.py
# @Desc    :


from sklearn.feature_extraction.text import CountVectorizer
import sklearn
import numpy as np

vectorizer = CountVectorizer()
content = ["How to format my hard disk", " Hard disk format problems"]
X = vectorizer.fit_transform(content)
print(vectorizer.get_feature_names())
print(X.toarray().transpose())

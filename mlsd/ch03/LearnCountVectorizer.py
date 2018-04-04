#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/04/03 14:23
# @Author  : c0l0121
# @File    : LearnCountVectorizer.py
# @Desc    :

import os
import sys
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import scipy as sp
import nltk.stem
import numpy as np

english_stemmer = nltk.stem.SnowballStemmer('english')


class StemmedCountVectorizer(CountVectorizer):
    """将文内单次转换为词干再统计次数

    """

    def build_analyzer(self):
        """重载父类方法以在分析时先把单词转换为词干

        :return:将单词转换为词干后的分析结果
        """
        analyzer = super(StemmedCountVectorizer, self).build_analyzer()
        return lambda doc: (english_stemmer.stem(w) for w in analyzer(doc))


class StemmedTfidfVectorizerCountVectorizer(TfidfVectorizer):
    """将文内单次转换为词干再统计"词频-反转文档频率"

    """

    def build_analyzer(self):
        """重载父类方法以在分析时先把单词转换为词干

        :return:将单词转换为词干后的分析结果
        """
        analyzer = super(TfidfVectorizer, self).build_analyzer()
        return lambda doc: (english_stemmer.stem(w) for w in analyzer(doc))


def dist_raw(v1, v2):
    """ 计算向量v1和v2的欧氏距离

    :param v1: 向量1
    :param v2: 向量2
    :return: 欧氏距离
    """
    delta = v1 - v2
    return sp.linalg.norm(delta.toarray())


def dist_normalized(v1, v2):
    """ 计算向量v1和v2归一化后的欧氏距离

    :param v1: 向量1
    :param v2: 向量2
    :return: 归一化后的欧氏距离
    """
    # 归一化
    v1_normalized = v1 / sp.linalg.norm(v1.toarray())
    v2_normalized = v2 / sp.linalg.norm(v2.toarray())
    delta = v1_normalized - v2_normalized
    return sp.linalg.norm(delta.toarray())


vectorizer = CountVectorizer()
content = ["How to format my hard disk", " Hard disk format problems"]
print("Content : %s" % content)
X = vectorizer.fit_transform(content)
print("Feature Names : %s" % vectorizer.get_feature_names())
print("#samples: %d, #features: %d" % X.shape)
print("Feature's count : \n %s" % X.toarray())

# 从文件读入语句
DIR = "./data/toy/"

# os.path.join(目录,文件) 将目录和文件结合到一起形成带文件的路径。
# open(文件路径) 打开文件
# open(文件路径).read() 读取内容
# os.listdir(目录) 列出目录下的文件
posts = [open(os.path.join(DIR, f)).read() for f in os.listdir(DIR)]
print("Posts : %s" % posts)
posts_vec = vectorizer.fit_transform(posts)
num_samples, num_features = posts_vec.shape
print("#samples: %d, #features: %d" % (num_samples, num_features))
print("Feature Names : %s" % vectorizer.get_feature_names())

new_post = "imaging databases"
new_post_vec = vectorizer.transform([new_post])
print("New post with vector:  %s            : %s" % (new_post_vec.toarray(), new_post))

# 计算与新帖子最接近的帖子
best_doc = None
best_dist = sys.maxsize
best_i = None

for i in range(num_samples):
    post = posts[i]
    if post == new_post:
        continue
    post_vec = posts_vec.getrow(i)
    d = dist_raw(post_vec, new_post_vec)
    print("=== Post %i with vector=%s, dist=%.2f : %s" % (i, posts_vec.getrow(i).toarray(), d, post))
    if d < best_dist:
        best_dist = d
        best_i = i

print("Best post is %i with dist=%.2f\n" % (best_i, best_dist))

# 归一化后，pos3和pos4有可以得到相同的距离
print("Calculate distance between new_post and postX after normalize.")
print("New post with vector:  %s            : %s" % (new_post_vec.toarray(), new_post))
for i in range(num_samples):
    post = posts[i]
    if post == new_post:
        continue
    post_vec = posts_vec.getrow(i)
    d = dist_normalized(post_vec, new_post_vec)
    print("=== Post %i with vector=%s, dist=%.2f : %s" % (i, posts_vec.getrow(i).toarray(), d, post))
    if d < best_dist:
        best_dist = d
        best_i = i

print("Best post is %i with dist=%.2f\n" % (best_i, best_dist))

print("Remove unimportant words by using 'stop_words' param when instance CountVectorizer.")
vectorizer = CountVectorizer(stop_words='english')
print("Stop words in 'english' (first 20): %s" % sorted(vectorizer.get_stop_words())[0:20])
posts_vec = vectorizer.fit_transform(posts)
new_post_vec = vectorizer.transform([new_post])
print("Feature Names : %s" % vectorizer.get_feature_names())
print("New post with vector:  %s            : %s" % (new_post_vec.toarray(), new_post))
for i in range(num_samples):
    post = posts[i]
    if post == new_post:
        continue
    post_vec = posts_vec.getrow(i)
    d = dist_normalized(post_vec, new_post_vec)
    print("=== Post %i with vector=%s, dist=%.2f : %s" % (i, posts_vec.getrow(i).toarray(), d, post))
    if d < best_dist:
        best_dist = d
        best_i = i

print("Best post is %i with dist=%.2f\n" % (best_i, best_dist))

print("")
vectorizer = StemmedCountVectorizer(min_df=1, stop_words='english')
posts_vec = vectorizer.fit_transform(posts)
new_post_vec = vectorizer.transform([new_post])
print("Feature Names : %s" % vectorizer.get_feature_names())
print("New post with vector:  %s            : %s" % (new_post_vec.toarray(), new_post))
for i in range(num_samples):
    post = posts[i]
    if post == new_post:
        continue
    post_vec = posts_vec.getrow(i)
    d = dist_normalized(post_vec, new_post_vec)
    print("=== Post %i with vector=%s, dist=%.2f : %s" % (i, posts_vec.getrow(i).toarray(), d, post))
    if d < best_dist:
        best_dist = d
        best_i = i

print("Best post is %i with dist=%.2f\n" % (best_i, best_dist))

vectorizer = StemmedTfidfVectorizerCountVectorizer(min_df=1, stop_words='english')
posts_vec = vectorizer.fit_transform(posts)
new_post_vec = vectorizer.transform([new_post])
print("Feature Names : %s" % vectorizer.get_feature_names())
print("New post with vector:  %s            : %s" % (np.round(new_post_vec.toarray(), 2), new_post))
for i in range(num_samples):
    post = posts[i]
    if post == new_post:
        continue
    post_vec = posts_vec.getrow(i)
    d = dist_normalized(post_vec, new_post_vec)
    print("=== Post %i with vector=%s, dist=%.2f : %s" % (i, np.round(posts_vec.getrow(i).toarray(), 2), d, post))
    if d < best_dist:
        best_dist = d
        best_i = i

print("Best post is %i with dist=%.2f" % (best_i, best_dist))

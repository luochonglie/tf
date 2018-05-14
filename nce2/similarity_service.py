#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/05/14 18:16
# @Author  : c0l0121
# @File    : similarity_service.py
# @Desc    :


import mysql.connector


class Similarity(object):
    def __init__(self, file_name, similarity):
        self.file_name = file_name
        self.similarity = similarity


def __get_connection():
    # 打开数据库连接
    # 用户名:hp, 密码:Hp12345.,用户名和密码需要改成你自己的mysql用户名和密码，并且要创建数据库TESTDB，并在TESTDB数据库中创建好表Student
    conn = mysql.connector.connect(host='47.95.117.152', user="nce", passwd="nce", database="nce", use_unicode=True)
    return conn


def __close_connection(conn):
    if conn is not None:
        conn.close()


def insert(similarity):
    conn = __get_connection()
    sql = "insert into similarity(file_name, date, similarity) values(%s, sysdate(), %s)"
    conn.cursor().execute(sql, [similarity.file_name, similarity.similarity])
    conn.commit()
    __close_connection(conn)


if __name__ == '__main__':
    similarity = Similarity('a', 50)
    insert(similarity)

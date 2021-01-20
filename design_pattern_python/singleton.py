#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   singleton.py
@Time    :   2021/01/20 09:52:06
@Author  :   Ayden Zeng
@Version :   1.0
@Contact :   aydenzeng@163.com
@License :   (C)Copyright 2020-2021, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
from abc import abstractclassmethod, ABCMeta

class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

class Myclass(Singleton):
    def __init__(self, a):
        self.a = a

a = Myclass(10)
b = Myclass(20)

print(a.a)  # 20
print(b.a)  # 20

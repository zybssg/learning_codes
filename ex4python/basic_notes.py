#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   basic_notes.py
@Time    :   2021/01/21 16:19:58
@Author  :   Ayden Zeng
@Version :   1.0
@Contact :   aydenzeng@163.com
@License :   (C)Copyright 2020-2021, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
import sys
import getopt
import random


# class Fab:
#     def __init__(self, n):
#         self.n = n
#         self.now = 0
#         self.first = 0
#         self.second = 1

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.now < self.n:
#             self.out = self.first
#             self.first, self.second = self.second, self.first + self.second
#             self.now += 1
#             return self.out
#         else:
#             raise StopIteration


# # client
# myfab = Fab(10)
# myfab_iter = iter(myfab)
# while True:
#     try:
#         print(next(myfab_iter))
#     except StopIteration:
#         break


def fab(n):
    first, second = 0, 1
    now = 0
    while now < n:
        yield first
        first, second = second, first + second
        now += 1

myfab = fab(10)
print(myfab)
while True:
    try:
        print(next(myfab))
    except StopIteration:
        break
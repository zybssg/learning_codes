#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   chain_of_responsibility.py
@Time    :   2021/01/25 10:28:01
@Author  :   Ayden Zeng
@Version :   1.0
@Contact :   aydenzeng@163.com
@License :   (C)Copyright 2020-2021, Ayden-Zeng-Private
@Desc    :   None
'''

# here put the import lib
from abc import abstractmethod, ABCMeta

class Handler(metaclass=ABCMeta):
    @ abstractmethod
    def handle_leave(self, day):
        pass


class GeneralManager(Handler):
    def handle_leave(self, day):
        if day <= 10:
            print("总经理批准请假%d天" % day)
        else:
            print("总经理建议辞职")


class DepartmentManager(Handler):
    def __init__(self):
        self.next = GeneralManager()

    def handle_leave(self, day):
        if day <= 5:
            print("部门经理批准请假%d天" % day)
        else:
            print("部门经理无此权限")
            self.next.handle_leave(day)


class ProjectManager(Handler):
    def __init__(self):
        self.next = DepartmentManager()

    def handle_leave(self, day):
        if day <= 2:
            print("项目经理批准请假%d天" % day)
        else:
            print("项目经理无此权限")
            self.next.handle_leave(day)


# client
day = 14
handler = ProjectManager()
handler.handle_leave(day)

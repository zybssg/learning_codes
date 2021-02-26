#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   observer.py
@Time    :   2021/01/26 19:20:18
@Author  :   Ayden Zeng
@Version :   1.0
@Contact :   aydenzeng@163.com
@License :   (C)Copyright 2020-2021, Ayden-Zeng-Private
@Desc    :   None
'''

# here put the import lib
from abc import abstractclassmethod, ABCMeta

# 抽象的发布者
class Notice(metaclass=ABCMeta):
    def __init__(self):
        self.observers = []

    # 订阅
    def attach(self, obs):
        self.observers.append(obs)

    # 取消订阅
    def detach(self, obs):
        self.observers.remove(obs)

    def notify(self):
        for obs in self.observers:
            obs.update(self)  #把自己self传进去


# 抽象的订阅者
class Observer(metaclass=ABCMeta):
    @abstractclassmethod
    def update(self, notice):
        pass


# 真实的发布者：公司信息发布系统
class CompanyNotice(Notice):
    def __init__(self, company_info=None):
        super().__init__()
        self.__company_info = company_info  # 设置为私有

    @property
    def company_info(self):
        return self.__company_info

    @company_info.setter
    def company_info(self, info):
        self.__company_info = info
        self.notify()


# 真实的订阅者：公式员工
class Staff(Observer):
    def __init__(self):
        self.company_info = None

    def update(self, notice):
        self.company_info = notice.company_info


# Client
notice = CompanyNotice()
s1 = Staff()
s2 = Staff()
notice.attach(s1)
notice.attach(s2)
notice.company_info = "今天放假"
print(s1.company_info)  # 今天放假
print(s2.company_info)  # 今天放假
notice.detach(s2)
notice.company_info = "今天取消放假"
print(s1.company_info)  # 今天取消放假
print(s2.company_info)  # 今天放假

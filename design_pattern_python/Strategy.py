#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   Strategy.py
@Time    :   2021/01/26 20:15:34
@Author  :   Ayden Zeng
@Version :   1.0
@Contact :   aydenzeng@163.com
@License :   (C)Copyright 2020-2021, Ayden-Zeng-Private
@Desc    :   None
'''

# here put the import lib
from abc import abstractmethod, ABCMeta

class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass


class StrategyNormal(Strategy):
    def execute(self, person):
        print(f'使用StrategyNormal策略去处理{person}客户')


class StrategyVIP(Strategy):
    def execute(self, person):
        print(f'使用StrategyVIP策略去处理{person}客户')


class Context:
    def __init__(self, person, strategy):
        self.person = person
        self.strategy = strategy
    
    # 切换新的策略
    def set_strategy(self, strategy):
        self.strategy = strategy
    
    # 执行策略
    def do_strategy(self):
        self.strategy.execute(self.person)


# Client
p1 = "normal customer"
s_VIP = StrategyVIP()
s_normal = StrategyNormal()

context = Context(p1, s_normal)
context.do_strategy()  # 使用StrategyNormal策略去处理normal customer客户

context.set_strategy(s_VIP)  # 切换策略
context.do_strategy()  # 使用StrategyVIP策略去处理normal customer客户

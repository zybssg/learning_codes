#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   composite.py
@Time    :   2021/01/22 11:29:23
@Author  :   Ayden Zeng
@Version :   1.0
@Contact :   aydenzeng@163.com
@License :   (C)Copyright 2020-2021, Ayden-Zeng-Private
@Desc    :   None
'''

# here put the import lib
from abc import abstractmethod, ABCMeta

# 抽象组件
class Graphic(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass


# 叶子组件
class Point(Graphic):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "点(%d, %d)"%(self.x, self.y)

    def draw(self):
        print(self)


# 叶子组件
class Line(Graphic):
    def __init__(self, point1, point2):
        self.p1 = point1
        self.p2 = point2
    
    def __str__(self):
        return "线段[%s, %s]"%(self.p1, self.p2)
    
    def draw(self):
        print(self)


# 复合组件
class Picture(Graphic):
    def __init__(self, gra_list):
        self.children = []
        for g in gra_list:
            self.add(g)
    
    def add(self, graphic):
        self.children.append(graphic)
    
    def draw(self):
        print("=====================")
        for child in self.children:
            child.draw()
        print("=====================")


# client
p1 = Point(1, 1)
p2 = Point(2, 2)
l1 = Line((3, 3), (4, 4))
l2 = Line((5, 5), (6, 6))

pic1 = Picture([p1, l1])
pic2 = Picture([p2, l2])
pic3 = Picture([pic1, pic2])
pic1.draw()
pic2.draw()
pic3.draw()

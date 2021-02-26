#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   bridge.py
@Time    :   2021/01/21 10:55:50
@Author  :   Ayden Zeng
@Version :   1.0
@Contact :   aydenzeng@163.com
@License :   (C)Copyright 2020-2021, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
from abc import abstractmethod, ABCMeta

class Shape(metaclass=ABCMeta):
    def __init__(self, color):
        self.color = color
    
    @abstractmethod
    def draw(self):
        pass


class Color(metaclass=ABCMeta):
    @abstractmethod
    def paint(self, shape):
        pass


class Rectangle(Shape):
    name = "长方形"
    def draw(self):
        self.color.paint(self)

class Circle(Shape):
    name = "圆形"
    def draw(self):
        self.color.paint(self)


class Red(Color):
    def paint(self, shape):
        print("画一个红色的%s"%shape.name)


class Green(Color):
    def paint(self, shape):
        print("画一个绿色的%s"%shape.name)


# 客户端高层代码
shape1 = Rectangle(Red())
shape1.draw()

shape2 = Circle(Green())
shape2.draw()
